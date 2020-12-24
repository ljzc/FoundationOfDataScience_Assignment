from abc import ABC

from crawler.src.crawl_strategy.crawl_strategy import CrawlStrategy

search_dict = {"baidu_news":"https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd={keywords}AF&medium=0&x_bfe_rqs=03E80&x_bfe_tjscore=0.000000&tngroupname=organic_news&newVideo=12&rsv_dl=news_b_pn&pn={item_number}",
               "xinlang_news": "https://search.sina.com.cn/?q={keywords}c=news&from=&col=&range=title&source=&country=&size=10&stime=&etime=&time=&dpc=0&a=&ps=0&pf=0&page={page_no}",
               "tianya_bbs": "https://search.tianya.cn/bbs?q={keywords}&pn={page_no}",
               "lizhi_news": "https://so.jstv.com/?keyword={keywords}&page={page_no}",
               "xinhua_news": "http://qc.wa.news.cn/nodeart/list?nid=11147664&pgnum=1&cnt=10000&tp={page_no}&orderby=1"
               }

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
