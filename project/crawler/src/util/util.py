import chardet
from selenium import webdriver
from urllib import request

import requests


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


