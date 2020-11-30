import abc

class CrawlStrategy(object):
    r"""
    这个类是一个抽象类，需要被继承
    """
    @abc.abstractmethod
    def get_news_generator(self, url, news_cnt=None, *keywords):
        r"""
        :param url: 网页地址
        :param news_cnt: 搜索的最大数量
        :param keywords: 可能需要的关键词
        :return: generator function， 是一个用来不断返回新的网址链接的生成器
        """
        pass
