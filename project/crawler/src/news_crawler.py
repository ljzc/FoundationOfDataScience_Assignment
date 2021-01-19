import re
from crawler.src.news_parser.baidu_news_parser import *
from crawler.src.news_parser.tianya_news_parser import *
from crawler.src.news_parser.other_parser import *
from crawler.src.news_parser.lizhi_news_parser import *
from crawler.src.news_parser.xinlang_news_parser import *
from crawler.src.news_parser.weibo_parser import WeiboParser
from crawler.src.crawl_strategy.other_strategy import WeiboStrategy as WStra
import threading

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


def weibo_craw(start, end, project_path, headers=util.headers_3):
    parser = WeiboParser(headers)
    for page in range(start, end, 5):
        f = open(f"{project_path}\\resorce\\weibo_urls({page}页-{page + 4}页).txt", "r", encoding='utf-8')
        weibo_urls = f.read().split("\n")
        if weibo_urls[-1] == 'finished!':
            print(f"已完成的部分：weibo_urls({page}页-{page + 4}页).txt")
            continue
        f.close()
        for weibo_url in weibo_urls:
            try:
                if weibo_url == '':
                    continue
                weibo_news = parser.parse(weibo_url)
                file_name = "{time}_{title}".format(time=weibo_news.time.strftime("%Y-%m-%d"),
                                                    title=util.beautify(weibo_news.title))
                path = "{project_path}\\weibo_data".format(project_path=project_path)
                code = weibo_news.to_string()
                util.to_mark_down(code, path, file_name)
            except TypeError:
                f = open(f"{project_path}\\error.txt\\", "a", encoding='utf-8')
                f.write(f"{weibo_url}\n")
                f.close()
                print(f"一个错误发生在访问：{weibo_url} 时，已经将它添加进error.txt中等待处理。 任务继续...")
        f = open(f"{project_path}\\resorce\\weibo_urls({page}页-{page + 4}页).txt", "a", encoding='utf-8')
        f.write("finished!")
        f.close()
        print(f"已完成：weibo_urls({page}页-{page + 4}页).txt")

def multi_thread(tasks: list, project_path: str):
    for task in tasks:
        headers = task[0]
        start_page = task[1]
        end_page = task[2]
        thread = threading.Thread(target=weibo_craw, args=(start_page, end_page, project_path, headers))
        thread.start()


if __name__ == '__main__':
    # 1100-2557
    multi_thread([(util.headers_3, 1150, 1200)],
                 "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project")
