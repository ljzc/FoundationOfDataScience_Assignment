from abc import ABC
from datetime import datetime
from crawler.src.news import news
from crawler.src.news_parser.news_parser import NewsParser
from crawler.src.util import util
import time
import random
import re


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

    def parse_comments(self, pages: list):
        pass

    def parse_pages(self, pages: list):
        ret = {}
        main_news = pages[0].find(attrs={'class': 'c', 'id': 'M_'})
        ret['author'] = main_news.div.a.text
        main_content = main_news.find(name='span', attrs={'class': 'ctt'})
        ret['title'] = main_content.find_next(name='a') + main_content.find_next(name='a')
        text = main_content.text.split("。", 1)
        ret['lead'] = text[0]
        ret['main_text'] = text[1]
        time_str = main_news.find(name='span', attrs={'class': 'ct'}).text
        if re.match("^[0-9]{2}月[0-9]{2}日.*", time_str):
            time_str = "{year}年{other}".format(year=datetime.today().year, other=time_str).replace('\n', '').replace('\r', '')

        ret['time'] = datetime.strptime(time_str, "%Y年%m月%d日 %H:%M")
        ret['contents'] = self.parse_comments(pages)

        return ret


    def parse(self, url: str, **keywords) -> news:
        pass
