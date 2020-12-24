import chardet
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request
from requests_html import HTMLSession
import requests
from datetime import date
import crawler.src.util.html_constructor as html_cons

headers_1 = {
    'Cookie': 'SINAGLOBAL=8342053747702.012.1598857415409; '
              'SUB=_2A25y0eOwDeRhGeBO6VIW8S7IzjWIHXVuPY34rDV8PUJbkNANLULBkW1NSj2xDSfM_On3UOcSFN9o7V6rRexLe-_5; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhoB33PUeGRSyTAY8LWSCdC5NHD95Qcehz7S027Sh-4Ws4Dqcj3i--NiK.4i'
              '-i2i--RiKn4i-zEi--Ri-2pi-8hi--Ri-2pi-8Feo5pS05E; UOR=,,cn.bing.com; wvr=6; _s_tentry=cn.bing.com; '
              'Apache=5960090841135.644.1608721872186; '
              'ULV=1608721872224:8:3:1:5960090841135.644.1608721872186:1607831737835; '
              'webim_unReadCount=%7B%22time%22%3A1608721874169%2C%22dm_pub_total%22%3A4%2C%22chat_group_client%22'
              '%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A50%2C%22msgbox%22%3A0%7D ',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66 '
}

headers_2 = {
    'Cookie': 'SUB=_2A25y0eOwDeRhGeBO6VIW8S7IzjWIHXVuPY34rDV6PUJbktAKLXHWkW1NSj2xDQpaK_Cue_upUxB_GVKDp5Lzaep_; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhoB33PUeGRSyTAY8LWSCdC5NHD95Qcehz7S027Sh-4Ws4Dqcj3i--NiK.4i-i2i'
              '--RiKn4i-zEi--Ri-2pi-8hi--Ri-2pi-8Feo5pS05E; _T_WM=fd3c35281ac629c3f6d0020a95074b5d ',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66 '
}


# def detect_encoding(url, headers=None):
#     r"""
#
#     :param url: 网址
#     :param headers: 请求头
#     :return:
#     """
#     raw_data = request.urlopen(url).read()
#     return chardet.detect(raw_data)['encoding']


def set_encoding(response: requests.Response) -> str:
    r"""
    将response的编码设置为正确的编码
    :param response: 一个requests.Response对象
    :return: 该网页的编码类型
    """
    raw_data = response.content
    encoding = chardet.detect(raw_data)["encoding"]
    response.encoding = encoding
    return encoding


def get_code_of_rendered_page(url: str) -> str:
    r"""
    使用selenium来获取js渲染后的网页源代码
    :param url: 网页地址
    :return: 网页源代码
    """
    browser = webdriver.Chrome()
    browser.get(url)
    code = browser.page_source
    browser.close()
    return code


def get_code_of_rendered_page_2(url: str) -> str:
    session = HTMLSession()
    r = session.get(url)
    # r.html.render()
    encoding = chardet.detect(r.content)["encoding"]
    return str(r.content, encoding=encoding)


def to_mark_down(code, path="news_info", name=""):
    if name == "":
        name = "default_" + date.today().strftime("%Y-%m-%d")
    f = open("{path}\\{name}.md".format(path=path, name=name), "w", encoding="utf-8")
    f.write(code)
    f.close()


def get_weibo_page(url: str) -> BeautifulSoup:
    response = requests.get(url, headers=headers_2)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup
