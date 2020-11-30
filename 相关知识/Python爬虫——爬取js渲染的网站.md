# Python爬虫——爬取js渲染的网站

[[Python3 网络爬虫开发实战\] 7.1-Selenium 的使用 | 静觅 (cuiqingcai.com)](https://cuiqingcai.com/5630.html)

主要使用Selenuim库配合ChromeDriver来获取选浏览器选然后的源代码, 这个方法是通过驱动浏览器, 用电脑模拟人来操作浏览器做到所见即所得, 这很方便, 但也正因如此, 这样会使得爬虫的速度变慢, 需要做好权衡.

### 准备工作

- 安装Chrome浏览器

  略

- [安装ChromeDriver](https://cuiqingcai.com/5135.html)

  1. 在Chrome浏览器地址栏中输入：

     ```
     chrome://settings/help
     ```

     或者点击菜单->帮助->关于Chrome打开关于Chrome页面

  2. 记下版本号:

     ```
     版本 87.0.4280.66（正式版本） （64 位）//这是我的版本号
     ```

  3. 在官网选择合适你Chrome版本号的下载链接, 点击打开镜像下载安装包

     官网下载链接: [Downloads - ChromeDriver - WebDriver for Chrome (chromium.org)](https://chromedriver.chromium.org/downloads)

     >这里是以上版本号的chromedriver安装包, 如果你的版本和我一样, 可以直接使用:
     >
     > [chromedriver_win32.zip](reference\rest\chromedriver_win32.zip) 

- 安装Seleniu库

  ```
  pip3 install selenium
  ```

### 最基本使用

由于我们只需要获得js渲染出的网页源代码, 并不需要进行网页交互, 所以这里只介绍最为基本的使用方法, 其他方法在有需求时再去查询.

```python

```

