import random

import chardet
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request
import requests
from datetime import date
import time
import os
import datetime
from crawler.src.news import news
headers_0 = {


    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66 '
}




headers_1 = {
    'Cookie': '_T_WM=0c1a41709a5fff9c7701d3964bb29a7e; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW.uPDJyarNIZ2OOcy23qvu5NHD95QEeKq41K2EeoqEWs4Dqcj6i--RiKn7iKnfi--ci-z0iK.ci--4iKL2iK.Ei--ci-2EiKnfi--fiK.EiKyhi--Ni-iFi-isi--RiKyhi-zc; SUB=_2AkMXVEXKdcPxrAFQnvEczWngao9H-jykgSw8An7oJhMyPRhu7lIJqSdutBF-XKxpahFXagwJ2zCmDtxgh9yhxKN-',

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

headers_4 = {
    'Cookie': '_T_WM=0c1a41709a5fff9c7701d3964bb29a7e; '
              'SUB=_2A25NDALmDeRhGeBO7FYY-CbEwj6IHXVuDq6urDV6PUJbktANLU7mkW1NRboZimSh1pVU5Zq7KxKULCHCzZ58nCUP; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWG6adMX-0buMXSXpWnGJUq5NHD95QcehMX1KnR1h.EWs4Dqcj6i--ciK.Ni-27i'
              '--ci-zpiKnEi--fiKLFi-i2i--4iK.4iKnfi--Ni-8Fi-27i--fi-2Xi-24i--fiK.0iK.4; SSOLoginState=1611166390 ',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75 '

}

headers_5 = {
    'Cookie': '_T_WM=80dedbbe93486578fe949da3a8af3292; '
              'SUB=_2A25NDJu6DeRhGeRP7VsY8SzOzT6IHXVuDiXyrDV6PUJbktANLW_gkW1NUB9_DG97Tn200WJ3yAgV0jacsNCHL3Fy; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW.uPDJyarNIZ2OOcy23qvu5NHD95QEeKq41K2EeoqEWs4Dqcj6i--RiKn7iKnfi'
              '--ci-z0iK.ci--4iKL2iK.Ei--ci-2EiKnfi--fiK.EiKyhi--Ni-iFi-isi--RiKyhi-zc; SSOLoginState=1611197418 '
              '-z0iK.ci--4iKL2iK.Ei--ci-2EiKnfi--fiK.EiKyhi--Ni-iFi-isi--RiKyhi-zc; SSOLoginState=1611166960',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.96 Safari/537.36 '
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
        f = open("{path}\\{name}.md".format(path=path,
                                            name=f"{date.today().strftime('%Y-%m-%d')}_原命名不合法_{round(1000000 * datetime.datetime.now().timestamp())}_{round(random.random()*100000000000 )}"),
                 "w",
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



