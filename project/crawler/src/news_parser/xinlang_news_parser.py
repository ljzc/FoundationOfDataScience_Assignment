from abc import ABC

from crawler.src.news import news
from crawler.src.news_parser.news_parser import NewsParser


class XinLangNewsParser(NewsParser, ABC):
    r"""
    新浪新闻网页解析器
    """
    def parse(self, url: str, **keywords) -> news:
        r"""
        解析新浪新闻网页
        :param url:
        :param keywords:
        :return:
        """
        # todo
        pass