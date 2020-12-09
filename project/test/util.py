from bs4 import BeautifulSoup
import requests
import datetime
from crawler.src.util.util import set_encoding
def into_file(soup : BeautifulSoup):
    file_name = "html_code\\" + soup.title.string + datetime.datetime.now().strftime("(%Y-%m-%d)") + ".html"
    f = None
    try:
        f = open(file_name, "w",encoding="utf-8")
    except OSError:
        f = open("html_code\\" + "invalid_file_name" + datetime.datetime.now().strftime("(%Y-%m-%d)") + ".html","w",encoding="utf-8")

    f.write(soup.prettify())

if __name__ == '__main__':
    response = requests.get("https://k.sina.com.cn/article_6192937794_17120bb4202001fpcb.html?from=news&subch=onews")
    set_encoding(response)


    into_file(BeautifulSoup(response.text, "lxml"))
