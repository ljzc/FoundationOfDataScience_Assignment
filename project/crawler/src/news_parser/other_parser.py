from abc import ABC

from crawler.src.news.news import News
from crawler.src.news_parser.news_parser import NewsParser


class SiChuanNews(NewsParser, ABC):
    r"""
    示例url：

    """

    def parse(self, url: str, **keywords) -> News:
        # todo
        pass


class PenpaiNews(NewsParser, ABC):
    r"""
    示例ulr：
    https://www.thepaper.cn/newsDetail_forward_10329137

    评论：有
    """

    def parse(self, url: str, **keywords) -> News:
        # todo
        pass
