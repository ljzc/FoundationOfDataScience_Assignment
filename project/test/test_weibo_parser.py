from crawler.src.news import news
from test.util import into_file
from test.util import into_soup
from crawler.src.news_parser.weibo_parser import WeiboParser


def test_pages_of():
    pages = WeiboParser().pages_of("https://weibo.cn/comment/J7dzH65LJ")
    i = 1
    for page in pages:

        into_file(page, mark="第{pageNO}页".format(pageNO=i))
        i += 1

def test_parse_pages():
    pages = []
    path = 'D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\test' \
           '\\html_code\\评论列表(2021-01-19)_第{pageNO}页.html '
    for i in range(1, 13):
        pages.append(into_soup(path.format(pageNO=i)))
    result = WeiboParser().parse_pages(pages)
    ret = news.News(result['time'], result['author'], "test", False, None, news._NewsTypes.CENTRAL_MEDIA,
              result['comments'], result['title'], result['lead'], result['main_text'], result['attrs'])
    f = open("D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\test\\news_info\\default_2020-12-10.md", "w", encoding="utf-8")
    f.write(ret.to_string())
    f.close()

def test_parse_local():
    f = open(
        "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\test\\news_info\\default_2020-12-10.md",
        "r", encoding="utf-8")
    raw = f.read()
    f.close()
    parsed = news.parse_from_info(raw)
    f = open("D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\test\\news_info\\out_.md",
        "w", encoding="utf-8")
    f.write(parsed.to_string())
    f.close()
    return None