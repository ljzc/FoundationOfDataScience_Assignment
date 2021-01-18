from datetime import datetime, date
from crawler.src.news.comment import Comment, Comments, parse_comment_block
import crawler.src.util.html_constructor as html_cons
from bs4 import BeautifulSoup
from crawler.src.util.util import beautify

def parse_location(location_info):
    pass

def parse_analyse(analyse_info):
    pass

def parse_from_info(news_info):
    r"""
    将一个由to_string()方法格式化的字符串解析成一个News对象，返回该对象
    """
    soup = BeautifulSoup(news_info)
    title = soup.find(attrs={"id": "title"}).text
    time = soup.find(attrs={"id": "time"}).text
    time = datetime.strptime(beautify(time), "%Y-%m-%d")
    author = soup.find(attrs={"id" : "author"}).text
    src = soup.find(attrs={"id": "src"}).a.attrs["href"]
    render = bool(beautify(soup.find(attrs={"id" : "is_rendered"}).text).split(" ")[1])
    location = parse_location(soup.find(attrs={"id": "location"}))
    news_type = beautify(soup.find(attrs={"id": "news_type"}).text).split(" ", 1)[1]
    attrs_li = soup.find(attrs={"id": "attrs"}).find_all(name="li")
    attrs = {"repost": int(beautify(attrs_li[0].text).split(" ")[1]),
             "comment_number": int(beautify(attrs_li[1].text).split(" ")[1]),
             "attitude": int(beautify(attrs_li[2].text).split(" ")[1])}
    lead = soup.find(attrs={"id" : "lead"}).strong.text
    main_text = []
    for p in soup.find(attrs={"id" : "main_text"}).find_all(name="p"):
        main_text.append(beautify(p.text))
    analyse = parse_analyse(soup.find(attrs={"id": "analyse_info"}))
    comments = parse_comment_block(soup.find(attrs={"id": "comments"}))
    return News(time, author, src, render, location, news_type, comments, title, lead, main_text, attrs)
    # todo
    pass

class News(object):
    r"""
    这是存放新闻的类，计划后期做数据分析的时候也用这个类。
    """





    def __init__(self,
                 time: date,
                 author: str,
                 src: str,
                 is_rendered: bool,
                 location: str,
                 news_type: str,
                 comments: Comments,
                 title: str,
                 lead: str,
                 main_text: list,
                 attrs=None
                 ):
        r"""
        :param time: 时间，注意参数类型
        :param author: 新闻的作者
        :param src: 新闻的来源，为了保留尽可能完整的信息，直接将该新闻的url传入（这样如果后期发现少了什么信息的话还有办法补救）
        :param is_rendered: 新闻网页是否采用了渲染方式（和src配套，为了后期能够更高效地补全我们漏掉的信息）
        :param location: 描述新闻地址的字符串
        :param news_type: 新闻类型，注意使用_NewsTypes类中定义好的常量
        :param comments:评论，注意传入Comments类的对象
        :param title: 标题
        :param lead: 导语
        :param main_text: 主体部分（除了导语外的正文部分）,一段是一个元素
        :param attrs: 相关参数，例如转赞评
        """
        # 保证新闻类型来自预先定义好的常量
        assert news_type == _NewsTypes.CENTRAL_MEDIA \
               or news_type == _NewsTypes.SELF_EMPLOYED_MEDIA \
               or news_type == _NewsTypes.WEB_NEWS_PLATFORM

        self.time = time
        self.author = author
        self.src = src
        self.is_rendered = is_rendered
        self.location = location
        self.news_type = news_type
        self.comments = comments
        self.title = title
        self.main_text = main_text
        self.lead = lead
        self.attrs = attrs

        # self.emotional_words = dict()
        self.emotional_vector = []
        self.psychology_vector = []
        self.is_significant = False
        self.summery = None
        self.event_type = ""

    def to_string(self) -> str:
        r"""
        将新闻格式化为一个字符串，以便于写入文件中
        :return: 一个格式化好的字符串，可以直接写入文件或者传入数据库储存起来的那种
        """
        # 标题
        title = html_cons.h1(self.title, id_no="title")

        # 基本信息
        time = html_cons.p(self.time.strftime("%Y-%m-%d"), id_no="time")
        author = html_cons.p(self.author, id_no="author")
        src = html_cons.p(id_no="src").add(html_cons.a("新闻链接", href=self.src))
        render = html_cons.p("渲染： {0}".format(self.is_rendered), id_no="is_rendered")
        location = html_cons.p("地点： {0}".format(self.location), id_no="location")  # 这个可能要改
        news_type = html_cons.p("类型： {0}".format(self.news_type), id_no="news_type")
        basic_info = html_cons.div(id_no="basic_info").add(html_cons.h2("基本信息：")) \
            .add(time).add(author).add(src).add(render).add(location).add(news_type)

        # 参数
        attrs = html_cons.div(id_no="attrs").add(html_cons.li("转发： {repost}".format(repost=self.attrs["repost"]), id_no="repost"))\
            .add(html_cons.li("评论数量： {comments}".format(comments=self.attrs["comment_number"]), id_no="comment_number"))\
            .add(html_cons.li("赞： {attitude}".format(attitude=self.attrs["attitude"]), id_no="attitude"))

        # 正文+导语
        lead = html_cons.p(id_no="lead").add(html_cons.strong(self.lead))
        main_text = html_cons.div(id_no="main_text")
        cnt = 1
        for p in self.main_text:
            main_text.add(html_cons.p(p, id_no="paragraph_{0}".format(cnt)))
            cnt += 1
        article = html_cons.div(id_no="article").add(html_cons.h2("新闻主体：")).add(lead).add(main_text)

        # 分析信息
        analyse = html_cons.div("分析信息，还没想好", id_no="analyse_info")

        # 评论
        comments = html_cons.div(id_no="comments").add(html_cons.h2("评论："))
        if self.comments is not None:
            comments = self.comments.format()

        return html_cons.html().add(html_cons.body()
                                    .add(title)
                                    .add(basic_info)
                                    .add(attrs)
                                    .add(article)
                                    .add(analyse)
                                    .add(comments)
                                    ).to_html_string()


class _NewsTypes(object):
    CENTRAL_MEDIA = "central media"
    SELF_EMPLOYED_MEDIA = "self-employed media"
    WEB_NEWS_PLATFORM = "web news platform"
