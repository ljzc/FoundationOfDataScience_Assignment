import chardet
from urllib import request


def detect_encoding(url, headers=None):
    r"""

    :param url: 网址
    :param headers: 请求头
    :return:
    """
    raw_data = request.urlopen(url).read()
    return chardet.detect(raw_data)['encoding']
