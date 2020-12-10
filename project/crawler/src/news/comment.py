import datetime
import crawler.src.util.html_constructor as html_cons
class Comment(object):
    r"""
    评论类， 用来储存新闻的评论
    """
    def __init__(self, time: datetime.date, content: str, author=""):
        r"""

        :param time: 评论发出的时间
        :param content: 评论的内容
        :param author: 评论的作者（我不知道记录作者会不会侵犯别人的权利....）
        """
        self.time = time
        self.content = content
        self.author = author

    def format(self) -> html_cons.Tag:
        time = html_cons.p(self.time.strftime("%Y-%m-%d"), id_no="comment_time")
        author = html_cons.p(self.author, id_no="comment_author")
        content = html_cons.p(self.content)
        analyse = html_cons.div("用于分析的数据，还没想好", id_no="comment_analyse_info")
        comment = html_cons.div(id_no="comment").add(time).add(author).add(content).add(analyse)
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
        
