import abc

from src.news import news


class NewsParser(object):
    '''
    判断这个url下的新闻是否为符合要求的：文字版新闻
    如果不是符合要求的，返回None
    如果符合要求，对该新闻进行解析，返回一个news对象
    '''

    @abc.abstractmethod
    def parse(self, url: str) -> news:
        pass
