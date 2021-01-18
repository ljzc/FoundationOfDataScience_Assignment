from datetime import datetime
import crawler.src.util.html_constructor as html_cons
from bs4 import BeautifulSoup
from crawler.src.util.util import beautify


def parse_analyse_info(analyse_info):
    pass


def parse_comment_block(comment_block: BeautifulSoup):
    if comment_block is None:
        return None
    else:
        comments = Comments()
        for comment_info in comment_block.findAll(attrs={"id": "comments_block"}):
            comments.add_comment(parse_comment(comment_info))
        return comments


def parse_comment(comment_info: BeautifulSoup):
    time_str = beautify(comment_info.find(attrs={"id": "comment_time"}).text)
    time = datetime.strptime(time_str, "%Y-%m-%d")
    author = comment_info.find(attrs={"id": "comment_author"}).text
    attrs_li = comment_info.find(attrs={"id": "comment_attrs"}).find_all(name="li")
    attrs = {"is_hot": beautify(attrs_li[0].text).split(" ")[1] == "True",
             "attitude": int(beautify(attrs_li[1].text).split(" ")[1])}
    content = comment_info.find(attrs={"id": "comment_content"}).text
    analyse = parse_analyse_info(comment_info.find(attrs={"id": "comment_analyse_info"}))
    return Comment(time, content, author, attrs=attrs)


class Comment(object):
    r"""
    评论类， 用来储存新闻的评论
    """

    def __init__(self, time: datetime.date, content: str, author="", attrs=None):
        r"""

        :param time: 评论发出的时间
        :param content: 评论的内容
        :param author: 评论的作者（我不知道记录作者会不会侵犯别人的权利....）
        :param attrs: 评论参数，例如是否热门，赞数量等
        """
        self.time = time
        self.content = content
        self.author = author
        self.attrs = attrs

    def format(self) -> html_cons.Tag:
        time = html_cons.p(self.time.strftime("%Y-%m-%d"), id_no="comment_time")
        author = html_cons.p(self.author, id_no="comment_author")
        attrs = html_cons.div(id_no="comment_attrs").add(
            html_cons.li("是否热门： {hot}".format(hot=self.attrs["is_hot"]), id_no="is_hot")) \
            .add(html_cons.li("赞： {attitude}".format(attitude=self.attrs["attitude"]), id_no="attitude"))
        content = html_cons.p(self.content, id_no="comment_content")
        analyse = html_cons.div("用于分析的数据，还没想好", id_no="comment_analyse_info")
        comment = html_cons.div(id_no="comments_block").add(time).add(author).add(attrs).add(content).add(analyse)
        return comment


class Comments(object):
    r"""
    这是一个评论的集合，是对list的封装，这样做主要是为了指定传入参数的类型
    """

    def __init__(self):
        self.comments = []

    def add_comment(self, comment: Comment):
        self.comments.append(comment)
        return self

    def format(self) -> html_cons.Tag:
        comments = html_cons.div(id_no="comments").add(html_cons.h2("评论："))
        for c in self.comments:
            comments.add(c.format()).add(html_cons.hr())
        return comments
