import random

import chardet
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request
import requests
from datetime import date
import time

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

headers_3 = {
    'Cookie': '_T_WM=0c1a41709a5fff9c7701d3964bb29a7e; WEIBOCN_WM=3349; H5_wentry=H5; '
              'backURL=https%3A%2F%2Fweibo.cn%2F; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFWO5gkn9V9_sCCeVAnKCIr5NHD95QNSK-pSheE1h24Ws4DqcjMi--NiK.Xi-2Ri'
              '--ciKnRi-zNS0-feKB0eonp1Btt; '
              'SUB=_2A25NASSJDeRhGeFL7lMV8yzEyjWIHXVuCkzBrDV6PUJbktAKLW36kW1Nfe4wC2a6zuHCt_0MEhgrwr9cNWVNkOUf; '
              'SSOLoginState=1610962137 ',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75 '

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


# def get_code_of_rendered_page_2(url: str) -> str:
#     session = HTMLSession()
#     r = session.get(url)
#     # r.html.render()
#     encoding = chardet.detect(r.content)["encoding"]
#     return str(r.content, encoding=encoding)


def to_mark_down(code, path="news_info", name=""):
    if name == "":
        name = "default_" + date.today().strftime("%Y-%m-%d")
    f = None
    try:
        f = open("{path}\\{name}.md".format(path=path, name=name), "w", encoding="utf-8")
    except OSError:
        f = open("{path}\\{name}.md".format(path=path, name=f"{date.today().strftime('%Y-%m-%d')}_原命名不合法"), "w",
                 encoding="utf-8")
    f.write(code)
    f.close()


def get_weibo_page(url: str, headers=headers_3) -> BeautifulSoup:
    response = requests.get(url, headers=headers)
    # print("状态码：{code}".format(code=response.status_code))
    while response.status_code != 200 or response.text == '':
        sec = (50 + random.random() * 100)
        if response.status_code == 200:
            print("出现错误:{code}，等待{second}秒...".format(code=response.status_code, second=round(sec, 5)))
        elif response.text == '':
            print("页面为空， 等待{second}秒...".format(second=sec))
        time.sleep(sec)
        response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def beautify(raw: str) -> str:
    raw = raw.replace("\n", "").replace("\r", "")
    raw = raw.strip()
    return raw
