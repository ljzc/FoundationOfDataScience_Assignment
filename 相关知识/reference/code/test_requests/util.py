import chardet
from urllib import request
from bs4 import BeautifulSoup
import requests
from selenium import webdriver


def detect_encoding(url, headers=None):
    r"""

    :param url: 网址
    :param headers: 请求头
    :return:
    """
    raw_data = request.urlopen(url).read()
    print(chardet.detect(raw_data))
    return chardet.detect(raw_data)['encoding']


def set_encoding(response: requests.Response) -> str:
    r"""
    将response的编码设置为正确的编码
    :param response: 一个requests.Response对象
    :return: 该网页的编码类型
    """
    raw_data = response.content
    encoding = chardet.detect(raw_data)["encoding"]
    print("encoding ：", encoding)
    response.encoding = encoding
    return encoding




def output_to_file(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    f = open("source_code.html", "w")
    f.write(soup.prettify())
    f.close()


if __name__ == '__main__':
    raw_data = requests.get("http://news.jstv.com/a/20201130/1606733984697.shtml").content
    utf_8encoding = raw_data.decode("utf-8")
    print(utf_8encoding)
    f = open("source_code.html", "w",encoding="utf-8")
    f.write(utf_8encoding)
