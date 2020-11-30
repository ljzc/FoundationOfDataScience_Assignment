import datetime

class Comment(object):
    r"""
    评论类， 用来储存新闻的评论
    """
    def __init__(self, time: datetime.datetime, content: str, author=""):
        r"""

        :param time: 评论发出的时间
        :param content: 评论的内容
        :param author: 评论的作者（我不知道记录作者会不会侵犯别人的权利....）
        """
        self.time = time
        self.content = content
        self.author = author


class Comments(object):
    r"""
    这是一个评论的集合，是对list的封装，这样做主要是为了指定传入参数的类型
    """
    def __init__(self):
        self.comments = []

    def add_comment(self, comment: Comment):
        self.comments.append(comment)
