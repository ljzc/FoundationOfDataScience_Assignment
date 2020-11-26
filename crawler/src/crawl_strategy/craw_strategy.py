import abc


class CrawlStrategy(object):
    '''
    这个方法要求返回一个generator function, 每调用一次next就要返回一个将要被爬取的新闻url
    '''
    @abc.abstractmethod
    def get_news_generator(self, url, news_cnt, *keywords):
        pass
