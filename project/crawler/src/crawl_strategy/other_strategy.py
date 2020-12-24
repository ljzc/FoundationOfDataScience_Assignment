from abc import ABC

from crawler.src.crawl_strategy.crawl_strategy import CrawlStrategy
import time
from bs4 import BeautifulSoup
import requests
import datetime
from crawler.src.util.util import set_encoding
import crawler.src.util.util as util


def news_generator(home_page: str, start, end, headers=util.headers_2):
    for pageNO in range(start, end):
        soup = util.get_weibo_page(home_page.format(pageNO=pageNO))

        for blog in soup.find_all(attrs={'class': 'cc'}):
            yield blog.attrs['href'].split('?')[0]
        time.sleep(15)


class WeiboStrategy(CrawlStrategy, ABC):
    def get_news_generator(self, url, news_cnt=None, start_page=800, end_page=801, headers=util.headers_2, *keywords):
        home_page = url + '?page={pageNO}'
        return news_generator(home_page, start_page, end_page, headers=headers)
