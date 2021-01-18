from abc import ABC
from datetime import datetime
from crawler.src.news import news
from crawler.src.news_parser.news_parser import NewsParser
from crawler.src.util import util
from crawler.src.util.util import beautify
import time
import random
import re
from crawler.src.news.comment import Comment
from crawler.src.news.comment import Comments
from bs4 import BeautifulSoup


class WeiboParser(NewsParser, ABC):
    def pages_of(self, url: str):
        pages = []
        first = util.get_weibo_page("{base}?page={pageNO}".format(base=url, pageNO=1))
        end = int(first.find(attrs={'name': 'mp'}).attrs['value'])
        pages.append(first)
        for i in range(2, end + 1):
            sec = random.choice(range(5, 15))
            print("正在爬取{url}的第{pageNO}页，为了防止微博封号，请耐心等待{second}秒...".format(url=url, pageNO=i, second=sec))
            time.sleep(sec)
            cur = util.get_weibo_page("{base}?page={pageNO}".format(base=url, pageNO=i))
            pages.append(cur)
        return pages

    def parse_one_comment(self, comment_block: BeautifulSoup):
        time_str = beautify(comment_block.find(name='span', attrs={'class': 'ct'}).text).split(" ")[0]
        time = datetime.strptime(time_str, "%Y-%m-%d")
        content = beautify(comment_block.find(name='span', attrs={'class': 'ctt'}).text)
        author = comment_block.find(name='a').text
        attrs = {}
        target = str(comment_block.find(text=re.compile('.*赞\\[[0-9]+].*')))
        target = beautify(target)
        attrs['attitude'] = int(re.match(".*?([0-9]+).*?", target)[1])
        attrs['is_hot'] = comment_block.find(name='span', attrs={'class': 'kt'}) != None
        return Comment(time, content, author, attrs)

    def parse_comments(self, pages: list):
        comments = Comments()
        for page in pages:
            raw_commends = page.find_all(name='div', attrs={'class': 'c'})
            for raw in raw_commends:
                attrs = dict(raw.attrs)
                if (attrs.get("id", None) is not None) and (re.match("C_[0-9]+.*?", str(attrs.get("id"))) is not None):
                    comments.add_comment(self.parse_one_comment(raw))
        return comments

    def parse_pages(self, pages: list):
        ret = {}
        main_news = pages[0].find(attrs={'class': 'c', 'id': 'M_'})
        ret['author'] = beautify(main_news.div.a.text)
        main_content = main_news.find(name='span', attrs={'class': 'ctt'})
        ret['title'] = beautify(main_content.find_next(name='a').text + main_content.find_next(name='a').text)
        text = main_content.text.split("。", 1)
        ret['lead'] = beautify(text[0])
        ret['main_text'] = text[1].split("\n")
        time_str = main_news.find(name='span', attrs={'class': 'ct'}).text
        # if re.match("^[0-9]{2}月[0-9]{2}日.*", time_str):
        #     time_str = "{year}年{other}".format(year=datetime.today().year, other=time_str)
        time_str = beautify(time_str)
        time_str = re.match("^ *(.+?) *$", time_str)[1]
        ret['time'] = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")   .date()
        news_attrs = main_news.next_sibling.next_sibling.next_sibling.next_sibling
        ret['attrs'] = {}
        target = news_attrs.find(text=re.compile(".*转发\\[[0-9]+].*"))
        result = re.match(".*?([0-9]+).*?", str(target).replace("\n", "").replace(" ", ""))
        ret['attrs']['repost'] = int(result[1])
        target = news_attrs.find(text=re.compile(".*评论\\[[0-9]+].*"))
        result = re.match(".*?([0-9]+).*?", str(target).replace("\n", "").replace(" ", ""))
        ret['attrs']['comment_number'] = int(result[1])
        target = news_attrs.find(text=re.compile(".*赞\\[[0-9]+].*"))
        result = re.match(".*?([0-9]+).*?", str(target).replace("\n", "").replace(" ", ""))
        ret['attrs']['attitude'] = int(result[1])
        ret['comments'] = self.parse_comments(pages)
        return ret

    def parse(self, url: str, **keywords) -> news:
        result = self.parse_pages(self.pages_of(url))

        return news.News(result['time'], result['author'], url, False, None, news._NewsTypes.CENTRAL_MEDIA,
                         result['comments'], result['title'], result['lead'], result['main_text'], result['attrs'])

