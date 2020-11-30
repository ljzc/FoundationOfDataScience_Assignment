from abc import ABC

from src.news import news
from src.news_parser.news_parser import NewsParser
class BaiDuNewsParser(NewsParser, ABC):
    r"""
    百度新闻网页解析器
    """
    def parse(self, url: str, **keywords) -> news:
        r"""
        解析百度新闻网页
        :param url:
        :param keywords:
        :return:
        """
        # todo
        pass
