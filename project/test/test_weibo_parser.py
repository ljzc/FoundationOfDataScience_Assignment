from test.util import into_file
from crawler.src.news_parser.weibo_parser import WeiboParser


def test_pages_of():
    pages = WeiboParser().pages_of("https://weibo.cn/comment/IssuOoC5w")
    i = 1
    for page in pages:

        into_file(page, mark="第{pageNO}页".format(pageNO=i))
        i += 1