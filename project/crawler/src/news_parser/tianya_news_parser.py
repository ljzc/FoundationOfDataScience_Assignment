from abc import ABC

from src.news import news
from src.news_parser.news_parser import NewsParser

class TianYaNewsParser(NewsParser, ABC):
    r"""
    天涯新闻网站解析器
    """
    def parse(self, url: str, **keywords) -> news:
        r"""
        解析天涯新闻网页
        :param url:
        :param keywords:
        :return:
        """
        # todo
        pass