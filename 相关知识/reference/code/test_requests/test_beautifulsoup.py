from bs4 import BeautifulSoup
import requests
import util
import re
def basic_usage():
    response = requests.get("http://news.jstv.com/a/20201129/1606629502561.shtml")
    # response.encoding = util.detect_encoding("https://www.gdtv.cn/article/1e8b5240d9dd305983d13d2de2a8932b")
    encoding = util.set_encoding(response)
    soup = BeautifulSoup(response.text, 'lxml', from_encoding=encoding)
    print(soup.prettify())
    print(soup.title.string)

def get_attr():
    response = requests.get("http://news.jstv.com/a/20201129/1606629502561.shtml")
    # response.encoding = util.detect_encoding("https://www.gdtv.cn/article/1e8b5240d9dd305983d13d2de2a8932b")
    encoding = util.set_encoding(response)
    soup = BeautifulSoup(response.text, 'lxml', from_encoding=encoding)
    print(soup.title.name)
    print(soup.title.attrs)

def get_paragraph():
    response = requests.get("http://news.jstv.com/a/20201129/1606629502561.shtml")
    # response.encoding = util.detect_encoding("https://www.gdtv.cn/article/1e8b5240d9dd305983d13d2de2a8932b")
    encoding = util.set_encoding(response)
    soup = BeautifulSoup(response.text, 'lxml', from_encoding=encoding)
    print(soup.p)

def get_child():
    html = r"""
    <!doctype html>
<html>

<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width initial-scale=1'>
    <title></title>
</head>

<body>
    <h1>一级标题</h1>
    <h2>二级标题1</h2>
    <h2>二级标题2</h2>
    <h2>二级标题3</h2>
    <ul>
        <li>
            <p>项目1</p>
        </li>
        <li>
            <p>项目2</p>
            <ul>
                <li>
                    <p>项目2.1</p>
                </li>
                <li>
                    <p>项目2.2</p>
                    <p>项目2.2中的段落</p>
                </li>
                <li>
                    <p>项目2.3</p>
                    <p><a href=''>项目2.3中的地址</a></p>
                </li>

            </ul>
        </li>
        <li>
            <p>项目3</p>
        </li>

    </ul>
    <p>段落1</p>
    <p>段落2</p>
    <p>段落3</p>
</body>

</html>
    """
    #response = requests.get("http://news.jstv.com/a/20201129/1606629502561.shtml")
    # response.encoding = util.detect_encoding("https://www.gdtv.cn/article/1e8b5240d9dd305983d13d2de2a8932b")
    #encoding = util.set_encoding(response)
    soup = BeautifulSoup(html, 'lxml')
    #
    # # 使用嵌套选择
    # print(type(soup.body.h1))
    # print(soup.body.h1)

    # 使用关联选择
    # #  调用contents选择所有的直接子节点（是一个list）
    # print(soup.body.ul.contents)

    # #  调用children属性
    # print(soup.body.ul.children)
    # for index, tag in enumerate(soup.body.ul.children):
    #     print("index",index,": ",tag)

    # #  调用parent属性来获得某个节点的直接父节点
    # print(soup.body.ul.li.p.parent)

    #  选择兄弟节点
    print(soup.body.ul.li  # 第一个<li>
          .next_sibling    # 换行符号
          .next_sibling    # 第二个<li>
          )
    print(soup.body.previous_sibling  # 是个换行符号
          .previous_sibling  # 是head
          )
    print(list(soup.body.ul.next_siblings))
    print(list(soup.body.ul.ul.previous_siblings))

def find():
    response = requests.get("http://news.jstv.com/a/20201129/1606629502561.shtml")
    # response.encoding = util.detect_encoding("https://www.gdtv.cn/article/1e8b5240d9dd305983d13d2de2a8932b")
    encoding = util.set_encoding(response)
    soup = BeautifulSoup(response.text, 'lxml', from_encoding=encoding)
    print(soup.find_all(name='p', text=re.compile(".+")))
if __name__ == '__main__':
    find()