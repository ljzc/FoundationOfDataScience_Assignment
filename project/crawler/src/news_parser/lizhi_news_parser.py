import locale
from abc import ABC
import requests
import datetime
from crawler.src.news import news
from crawler.src.news.news import News
from crawler.src.news.news import _NewsTypes
from crawler.src.news_parser.news_parser import NewsParser
from crawler.src.util import util
from bs4 import BeautifulSoup
from bs4 import Tag
import re

class LiZhiNewsParser(NewsParser, ABC):
    r"""
    荔枝新闻网站解析器
    """


    def parse_news(self, article: Tag):
        title = article.h3.string
        time_str = article.find(name="span", attrs={"class": "time"}).string
        time = datetime.datetime.strptime(time_str[:len(time_str) - 1], "%Y年%m月%d日 %H:%M:%S")
        print(len(time_str))
        author = article.find(name="span", attrs={"class": "source"})
        content = article.find(name="div", attrs={"class" : "content"})
        paragraphs = content.find_all(text=re.compile(".*?[\u4E00-\u9FA5].*?"))
        lead = paragraphs[0].string
        main_text = ""
        for i in paragraphs[1:]:
            main_text = main_text + i.string + "\n"
        return title, time, author, lead, main_text



    def parse(self, url: str, **keywords) -> news:
        r"""
        解析荔枝新闻网页
        :param url:
        :param keywords:
        :return:
        """
        # todo
        # 观察网页代码可以知道，这个新闻网站的新闻内容没有经过渲染，所以直接使用requests模拟请求即可
        response = requests.get(url)
        util.set_encoding(response)
        soup = BeautifulSoup(response.text, "lxml")
        title, time, author, lead, main_text = self.parse_news(soup.find(name="div",attrs={'class': 'article'}))
        return News(time, author, url, False, None,_NewsTypes.WEB_NEWS_PLATFORM, None, title, lead, main_text)

