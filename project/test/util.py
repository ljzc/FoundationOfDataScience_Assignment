from bs4 import BeautifulSoup
import requests
import datetime
from crawler.src.util.util import set_encoding
import crawler.src.util.util as util


def into_file(soup: BeautifulSoup, encod='utf-8', mark=''):
    title = "default_title"
    if soup.title != None:
        title = soup.title.string
    file_name = "html_code\\" + title + datetime.datetime.now().strftime("(%Y-%m-%d)") + '_{mark}'.format(mark=mark) + ".html"
    f = None
    try:
        f = open(file_name, "w", encoding=encod)
    except OSError:
        f = open("html_code\\" + "invalid_file_name" + datetime.datetime.now().strftime("(%Y-%m-%d)") + '_{mark}'.format(mark=mark) + ".html", "w",
                 encoding=encod)

    f.write(soup.prettify())
    f.close()

def into_soup(path: str):
    f = open(path, 'r', encoding='utf-8')
    content = f.read(10000000000)
    f.close()
    return BeautifulSoup(content, 'lxml')



if __name__ == '__main__':
    # response = requests.get("https://weibo.cn/comment/JbKCVb4xU?page=2", headers=util.headers_2)
    # # encoding = set_encoding(response)
    #
    # # print(BeautifulSoup(response.content, "lxml", from_encoding=encoding))
    #
    # into_file(BeautifulSoup(response.text, "lxml"))
    # # code = util.get_code_of_rendered_page("https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=%E7%96%AB%E6%83%85%E6%B6%88%E6%81%AF&medium=0&x_bfe_rqs=03E80&x_bfe_tjscore=0.000000&tngroupname=organic_news&newVideo=12&rsv_dl=news_b_pn&pn=70")
    # # into_file(BeautifulSoup(code, "lxml"))
    print(into_soup(r'C:\Users\13622\OneDrive\文档\大二上\数据科学基础大作业\FoundationOfDataScience_Assignment\project\test\html_code\评论列表(2020-12-23)_第1页.html').contents)
