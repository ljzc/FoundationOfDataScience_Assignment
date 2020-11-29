# Python爬虫——基本库的使用

**reference:**

[Python3 网络爬虫开发实战教程 | 静觅 (cuiqingcai.com)](https://cuiqingcai.com/5052.html)

| 库名称         | 简介                                                         | api                                                          |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| urllib         | 是python内置的一个HTTP请求库，不需要额外安装即可使用。       |                                                              |
| requests       | 功能强大，使用方便，**建议直接看这个**（听说安装不是很方便， 可能需要翻墙...） | [官方文档](http://www.python-requests.org/)<br /><br />[中文文档](https://cn.python-requests.org/zh_CN/latest/) |
| Beautiful Soup | 解析网页代码的强大工具                                       | [中文文档](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/) |
| chardet        | 强大的编码推测工具                                           | [简介](#chardet库)                                           |













## urllib库



#### 四个模块

| 模块名称      | 模块简介                                                     |
| ------------- | ------------------------------------------------------------ |
| `request`     | 它是最基本的 HTTP 请求模块，可以用来模拟发送请求。就像在浏览器里输入网址然后回车一样，只需要给库方法传入 URL 以及额外的参数，就可以模拟实现这个过程了。 |
| `error`       | 异常处理模块，如果出现请求错误，我们可以捕获这些异常，然后进行重试或其他操作以保证程序不会意外终止。 |
| `parse`       | 一个工具模块，提供了许多 URL 处理方法，比如拆分、解析、合并等。 |
| `robotparser` | 主要是用来识别网站的 robots.txt 文件，然后判断哪些网站可以爬，哪些网站不可以爬，它其实用得比较少。 |

- `request`模块

  - `urlopen()`方法：

    - 方法api：

      ```python
      urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
      ```

    - 功能：

      完成最基本的简单网页的**GET**请求抓取。

    - 参数介绍：

      | 参数      | 类型                                                         | 含义                                                         |
      | --------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
      | `url`     | 字符串                                                       | 网址（URL）                                                  |
      | `data`    | 字节流（`bytes`）**注意**：可以使用`bytes()`函数将一个`str`类型转化成`bytes`类型。 | 如果选择传入该参数，则`urlopen()`方法发送的请求不再时一个**GET**类型的请求，而是一个**POST**类型的请求，该请求的提交方式为表单提交方式，表单数据中的参数名和参数值由该`data`参数决定。我们可以借助`urllib.parse.urlencode()`方法来以字典形式指定参数名和参数方法。 |
    | `timeout` | 超时时间                                                     | 超时以后会抛出URL Error异常                                  |

*（这个库好像不是特别好用...直接看下一个吧）*

## requests库



### 安装

使用以下命令安装:

```
pip install requests
```

如果安装失败, 请翻墙...或者尝试其他方式:

[[Python3 网络爬虫开发实战\] 1.2.1-Requests 的安装 | 静觅 (cuiqingcai.com)](https://cuiqingcai.com/5132.html)



### 基本用法

- 发送**GET**请求

  使用`request.get()`来模拟浏览器发送一个**GET**请求. 这个方法的参数和返回值简介如下:

  - `get(url, **kwargs)`[[源代码\]](https://cn.python-requests.org/zh_CN/latest/_modules/requests/sessions.html#Session.get)

    Sends a GET request. Returns [`Response`](https://cn.python-requests.org/zh_CN/latest/api.html#requests.Response) object.

    | 参数:     | **url** -- URL for the new [`Request`](https://cn.python-requests.org/zh_CN/latest/api.html#requests.Request) object. <br />***\*kwargs** -- Optional arguments that `request` takes.(使用字典的形式传入该参数) |
    | :-------- | ------------------------------------------------------------ |
    | 返回类型: | [requests.Response](https://cn.python-requests.org/zh_CN/latest/api.html#requests.Response)类型的对象, 其中储存了从服务器返回的 |

  - 应用举例

    ```python
    import requests
    
    def get_without_keywords():
        # 发送一个简单的GET请求， 不在url中设置参数
        response = requests.get("https://www.gdtv.cn/article/be9dfdbc758ff7adb416760382702aa0")
        print(type(response))
        print(type(response.text))
        print(response.text)
        print(type(response.cookies))
        print(response.cookies)
    ```

    运行结果:

    ```
    C:\Users\13622\AppData\Local\Programs\Python\Python38\python.exe C:/Users/13622/OneDrive/文档/大二上/数据科学基础大作业/FoundationOfDataScience_Assignment/相关知识/reference/code/test_requests/test_get.py
    <class 'requests.models.Response'>
    <class 'str'>
    <!DOCTYPE html>
    <html lang="zh">
    //为了文档的简洁, 省略源代码部分. 
    </html>
    <class 'requests.cookies.RequestsCookieJar'>
    <RequestsCookieJar[]>
    
    Process finished with exit code 0
    
    ```

    事实证明, 有些新闻网站的实际编码与header中标明的不一致. 似乎只要涉及到中文编码, 解析就会出问题.

    [chardet库](#chardet库)可以帮我们解决这个问题

    ```python
    def get_with_keywords():
        data = {
            'name': 'germey',
            'age': 22
        }
        r = requests.get("http://httpbin.org/get", params=data)  # 这是一个测试网站， 用来返回请求的一些信息，返回的是一个json字符串。
        print(r.text)
    ```

    结果:

    ```
    {
      "args": {
        "age": "22", 
        "name": "germey"
      }, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.25.0", 
        "X-Amzn-Trace-Id": "Root=1-5fc30b0f-26d1cf424e2eb98d642afde0"
      }, 
      "origin": "202.119.46.77", 
      "url": "http://httpbin.org/get?name=germey&age=22"
    }
    ```

    如果已知是网站返回的是一个json字符串, 可使用以下方法将该字符串解析成一个json字典:

    ```python
    print(r.json())
    ```

    结果:

    ```python
    {'args': {'age': '22', 'name': 'germey'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.25.0', 'X-Amzn-Trace-Id': 'Root=1-5fc30be8-443358b47d49d07905d6566a'}, 'origin': '202.119.46.77', 'url': 'http://httpbin.org/get?name=germey&age=22'}
    
    ```

- 添加**headers**

  访问某些网站时需要添加请求头中的参数, 可以用以下方法来添加请求头参数:

  ```python
  def get_with_header():
      headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
  
      }
      r = requests.get("https://www.zhihu.com/explore", headers=headers)
      print(r.text)
  ```

  打开浏览器(这里以谷歌浏览器为例), 访问任何一个网站, 按下`ctrl+shift+I `即可打开开发者工具:

![屏幕截图 2020-11-29 135630](reference/image/屏幕截图 2020-11-29 135630.jpg)

选择最上层`Network`一栏, 在下方表格中选择需要的一项点击进入(如果只是要查看请求头中一些常规的参数信息的话, 可以随意选一项进入):

![屏幕截图 2020-11-29 140015](reference/image/屏幕截图 2020-11-29 140015.jpg)

选择`Headers`一栏, 找到`Request Headers`即可查看其中的参数. 

在python代码中, 我们使用字典的形式指定请求头中的参数信息, 然后将其该字典对象传入requests库的方法中即可设置请求头.

- 发送**POST**请求

  使用`requests.post()`方法来发送一条**POST**类型的请求, 方法的api如下:

  ```python
  def post(url, data=None, json=None, **kwargs):
      r"""Sends a POST request.
  
      :param url: URL for the new :class:`Request` object.
      :param data: (optional) Dictionary, list of tuples, bytes, or file-like
          object to send in the body of the :class:`Request`.
      :param json: (optional) json data to send in the body of the :class:`Request`.
      :param \*\*kwargs: Optional arguments that ``request`` takes.
      :return: :class:`Response <Response>` object
      :rtype: requests.Response
      """
  
  
  ```

  

## Beautiful Soup



### 安装

由于教程推荐安装**lxml**来作为**Beautiful Soup**的解析器, 所以需要安装**lxml**和**Beautiful Soup**两个模块.

- lxml安装

  ```
  pip3 install lxml
  ```

- beautifu soup安装

  ```
  pip install beautifulsoup4
  ```

  

### 基本用法

```

```

## chardet库

[Python 爬虫使用Requests获取网页文本内容中文乱码 - 云+社区 - 腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1482003)

### 安装

```
pip install chardet
```

### 使用

```python
raw_data = urllib.urlopen('http://blog.csdn.net/sunnyyoona').read()
print chardet.detect(raw_data)  # {'confidence': 0.99, 'encoding': 'utf-8'}

raw_data = urllib.urlopen('http://www.jb51.net').read()
print chardet.detect(raw_data)  # {'confidence': 0.99, 'encoding': 'GB2312'}
```

使用这个方法可以完美解决编码问题

为了减少代码重复, 我在util中提供了如下方法:

```python
def detect_encoding(url, headers=None):
    r"""

    :param url: 网址
    :param headers: 请求头
    :return:
    """
    raw_data = request.urlopen(url).read()
    return chardet.detect(raw_data)['encoding']
```

使用前记得impot:

```python
from src.util import util
```

