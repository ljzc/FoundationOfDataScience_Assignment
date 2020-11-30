import abc

from src.news import news


class NewsParser(object):
    @abc.abstractmethod
    def parse(self, url: str, **keywords) -> news:
        r"""
        判断这个url下的新闻是否为符合要求的：文字版新闻；
        并根据判断的结果做相应的处理。
        :param url: 新闻网页地址
        :param keywords: 为了保证接口的稳定性，我加入了这个参数
        :return: 如果新闻符合要求，返回一个保存该新闻所有信息的news对象，否则返回None
        """
        pass

