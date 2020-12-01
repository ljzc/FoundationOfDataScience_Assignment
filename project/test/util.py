from bs4 import BeautifulSoup
import requests
import datetime
from crawler.src.util.util import set_encoding
def into_file(soup : BeautifulSoup):
    file_name = "html_code\\" + soup.title.string + datetime.datetime.now().strftime("(%Y-%m-%d)") + ".html"
    f = open(file_name, "w",encoding="utf-8")
    f.write(soup.prettify())

if __name__ == '__main__':
    response = requests.get("http://news.jstv.com/a/20201201/1606785884150.shtml")
    set_encoding(response)
    into_file(BeautifulSoup(response.text, "lxml"))
