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
from analyse.data_purify import keywords_in_news





keywords_of_taeget_news = [
    '新冠', '疫', '确诊', '病例', '医', '患者', '病人',
    '急诊', '防护服', '肺炎', '防控', '感染', '预防', '隔离',
    '武汉', '核酸检测'

]



class WeiboParser(NewsParser, ABC):
    def __init__(self, headers=util.headers_3, default_headers=util.headers_0):
        self.headers = headers
        self.default_headers = default_headers

    def pages_of(self, url: str, headers):
        pages = []
        first = util.get_weibo_page("{base}?page={pageNO}".format(base=url, pageNO=1), headers=headers)
        pages.append(first)
        temp = first.find(attrs={'name': 'mp'})
        end = 1
        if temp is not None:
            end = int(temp.attrs['value'])
        else:
            print(f"没有页数信息，默认1页，请确认：{url}")
            return pages

        for i in range(2, end + 1):
            sec = (0.05 + random.random() * 0.01)
            print("正在爬取{url}的第{pageNO}/{total}页".format(url=url, pageNO=i, total=end))
            time.sleep(sec)
            cur = util.get_weibo_page("{base}?page={pageNO}".format(base=url, pageNO=i), headers=self.headers)
            pages.append(cur)
        return pages

    def parse_one_comment(self, comment_block: BeautifulSoup):
        time_str = beautify(comment_block.find(name='span', attrs={'class': 'ct'}).text).split(" ")[0]
        weibo_time = None
        if re.match("[0-9]+月[0-9]+日", time_str):
            time_str = f"{2021}-{time_str.replace('月', '-').replace('日', '')}"
        weibo_time = datetime.strptime(time_str, "%Y-%m-%d")
        content = beautify(comment_block.find(name='span', attrs={'class': 'ctt'}).text)
        author = comment_block.find(name='a').text
        attrs = {}
        target = str(comment_block.find(text=re.compile('.*赞\\[[0-9]+].*')))
        target = beautify(target)
        attrs['attitude'] = int(re.match(".*?([0-9]+).*?", target)[1])
        attrs['is_hot'] = comment_block.find(name='span', attrs={'class': 'kt'}) != None
        return Comment(weibo_time, content, author, attrs)

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

        text = main_content.text

        if isinstance(main_content.nextSibling, str) and len(main_content.nextSibling) > 1:
            text = text + main_content.nextSibling
        text = beautify(text)
        text = re.split("[。]", text, 1)
        ret['lead'] = beautify(text[0])
        if len(text) > 1:
            ret['main_text'] = text[1].split("\n")
        else:
            ret['main_text'] = []
        time_str = main_news.find(name='span', attrs={'class': 'ct'}).text
        # if re.match("^[0-9]{2}月[0-9]{2}日.*", time_str):
        #     time_str = "{year}年{other}".format(year=datetime.today().year, other=time_str)
        time_str = beautify(time_str)
        time_str = re.match("^ *(.+?) *$", time_str)[1]
        ret['time'] = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").date()
        news_attrs = pages[0].find(attrs={"class": "pms"}).parent
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
        ret['attrs']['target'] = False
        ret['comments'] = self.parse_comments(pages)
        return ret

    def parse(self, url: str, **keywords) -> news:
        result = self.parse_pages(self.pages_of(url, self.default_headers))
        raw_news = news.News(result['time'], result['author'], url, False, None, news._NewsTypes.CENTRAL_MEDIA,
                         result['comments'], result['title'], result['lead'], result['main_text'], result['attrs'])
        if keywords_in_news(raw_news, keywords_of_taeget_news):
            print('关键词匹配, 继续爬取评论...')
            new_result = self.parse_pages(self.pages_of(url, self.headers))
            raw_news.comments = new_result['comments']
            raw_news.attrs['target'] = True
        else:
            print('关键词不匹配, 继续爬取其他url...')
            raw_news.attrs['target'] = False
        return raw_news

    def re_parse_main_news(self, news):
        ret = {}
        first = util.get_weibo_page("{base}".format(base=news.src), headers=self.default_headers)
        main_news = first.find(attrs={'class': 'c', 'id': 'M_'})
        main_content = main_news.find(name='span', attrs={'class': 'ctt'})
        news.title = beautify(main_content.find_next(name='a').text + main_content.find_next(name='a').text)
        text = main_content.text
        if isinstance(main_content.nextSibling, str) and len(main_content.nextSibling) > 1:
            text = text + main_content.nextSibling
        text = beautify(text)
        text = re.split("[。]", text, 1)
        news.lead = beautify(text[0])
        if len(text) > 1:
            news.main_text = text[1].split("\n")
        else:
            news.main_text = []
        return news