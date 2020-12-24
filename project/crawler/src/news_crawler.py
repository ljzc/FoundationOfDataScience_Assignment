import re
from crawler.src.news_parser.baidu_news_parser import *
from crawler.src.news_parser.tianya_news_parser import *
from crawler.src.news_parser.other_parser import *
from crawler.src.news_parser.lizhi_news_parser import *
from crawler.src.news_parser.xinlang_news_parser import *

parsers = {re.compile("^https://baijiahao\\.baidu\\.com/s\\?id=[0-9]+.+$"): BaiDuNewsParser(),
           re.compile("^https://epaper\\.scdaily\\.cn/shtml/scrb/[0-9]+/[0-9]+\\.shtml$"): SiChuanNews(),
           re.compile("^http://bbs\\.tianya\\.cn/post-[a-zA-Z]+-[0-9]+-[0-9]+\\.shtml$"): TianYaNewsParser(),
           re.compile("^http://news\\.jstv\\.com/a/[0-9]+/[0-9]\\.shtml$"): LiZhiNewsParser(),
           re.compile("^https://(news|k)\\.sina\\.com\\.cn/.*?\\.(html|shtml)"): XinLangNewsParser(),
           }


class NewsCrawler(object):

    def __init__(self):
        self.__crawl_strategies = dict()
        self.__news = dict()

    def __set_up_strategies(self):
        r"""
        用来在__craw_strategies属性中添加相应的爬取策略,格式为:
        {strategy_name: strategy}
        :return: None
        """
        pass

    def crawl(self, url, strategy):
        pass

    def export_news(self, abs_path):
        pass


class Source(object):
    BAIDU_NEWS = "news.baidu.com"
    XINLANG_NEWS = "news.sina.com.cn"
    TIANYA_NEWS = "bbs.tianya.cn"
    LIZHI_NEWS = "news.jstv"
    XINHUA_NEWS = "qc.wa.news.cn"


class Api(object):
    BAIDU_NEWS = "https://news.baidu.com/?cmd=1&class=reci"
    XINLANG_NEWS = "https://news.sina.com.cn/roll/#pageid=153&lid=2509&k=&num=50&page=1"
    TIANYA_NEWS = "http://bbs.tianya.cn/list.jsp?item=funinfo&grade=3&order=1"
    LIZHI_NEWS = "http://news.jstv.com/"
    XINHUA_NEWS = "http://qc.wa.news.cn/nodeart/list?nid=11147664&pgnum=1&cnt=10&tp=1&orderby=1"

#
# import requests
#
#
# # 我这里是将经纬度转换为地址，所以选用的是逆地理编码的接口。
# # https://restapi.amap.com/v3/geocode/regeo?
# # output=xml&location=116.310003,39.991957&key=<用户的key>&radius=1000&extensions=all
#
# # 高德地图
# def geocode1(location):
#     parameters = {'output': 'json', 'location': location, 'key': 'b65ac7bac54ed07220e8d05ab93ad469',
#                   'extensions': 'all'}
#     base = 'https://restapi.amap.com/v3/geocode/regeo'
#     response = requests.get(base, parameters)
#     answer = response.json()
#     print('url:' + response.url)
#     print(answer)
#     # return answer['regeocode']['formatted_address'], answer['regeocode']['roads'][0]['id'], answer['regeocode']['roads'][0]['name']
#
# if __name__ == '__main__':
#     geocode1("天安门")
#
