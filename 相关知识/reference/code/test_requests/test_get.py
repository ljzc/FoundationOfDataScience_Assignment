import requests
import re
import urllib.request as request
import chardet
import util
from bs4 import BeautifulSoup

def get_without_keywords():
    # 发送一个简单的GET请求， 不在url中设置参数
    response = requests.get("http://news.jstv.com/a/20201129/1606629502561.shtml")
    # response.encoding = 'gbk'
    # print(type(response))
    # print(type(response.text))
    # f = open("code.txt", 'w', encoding='gbk')
    # f.write(response.text)
    # ##print(bytes(response.text,"utf-8"))
    # print(type(response.cookies))
    # print(response.cookies)



def get_with_keywords():
    data = {
        'q': 'germey',
        #'age':
    }
    r = requests.get("http://httpbin.org/get", params=data)  # 这是一个测试网站， 用来返回请求的一些信息，返回的是一个json字符串。
    print(r.json())

def get_with_header():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'

    }
    r = requests.get("https://www.zhihu.com/explore", headers=headers)
    print(r.text)

def output_to_file(url):
    response = requests.get(url)
    encoding = util.set_encoding(response)
    response.encoding = encoding
    soup = BeautifulSoup(response.encoding, from_encoding=encoding)
    f = open("source_code.html", "w")
    f.write(soup.prettify())
    f.close()



if __name__ == '__main__':
    output_to_file()


