from abc import ABC

from crawler.src.crawl_strategy.crawl_strategy import CrawlStrategy


class BFSStrategy(CrawlStrategy, ABC):
    r"""
    该类是广度优先搜索策略类， 需要覆写CrawlStrategy类中的相应方法， 这也是该类对外暴露的唯一接口
    该类的主要功能是通过新闻网站上面的相关推送链接逐层遍历并返回网页url
    """

    def get_news_generator(self, url, news_cnt=None, *keywords):
        r"""

        :param url:
        :param news_cnt:
        :param keywords: 该方法暂时不需要接收关键词， 关键词的作用还需要后期商定
        :return:
        """
        # todo
        pass
