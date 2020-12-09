from abc import ABC

from crawler.src.crawl_strategy.crawl_strategy import CrawlStrategy


class SearchStrategy(CrawlStrategy, ABC):
    r"""
    这个类是搜索策略类，需要覆写CrawlStrategy中的方法，这也是该类对外暴露的唯一接口（至少目前是这样计划的）
    主要功能是通过新闻网页上面的搜索功能来搜索新闻，然后将搜索到的新闻url返回
    """

    def get_news_generator(self, url, news_cnt=None, *keywords):
        r"""
        :param url:
        :param news_cnt:
        :param keywords: 搜索所需要的关键词
        :return:
        """
        # todo
        pass
