from crawler.src.crawl_strategy.other_strategy import WeiboStrategy as WStra
import time
def test():
    weibo_generator = WStra().get_news_generator('https://weibo.cn/renminwang', start_page=1100, end_page=2557)
    for i in range(0, 5):
        url = next(weibo_generator)
        print("{index} : {url}".format(index=i, url=url))
