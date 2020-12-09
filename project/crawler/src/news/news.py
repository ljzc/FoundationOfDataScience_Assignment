import datetime
from crawler.src.news.comment import Comment, Comments
from crawler.src.util.pyh import *

class News(object):
    r"""
    这是存放新闻的类，计划后期做数据分析的时候也用这个类。
    """

    @staticmethod
    def parse(news_info):
        r"""
        将一个由to_string()方法格式化的字符串解析成一个News对象，返回该对象
        """
        # todo
        pass

    def __init__(self,
                 time: datetime.date,
                 author: str,
                 src: str,
                 is_rendered: bool,
                 location: str,
                 news_type: str,
                 comments: Comments,
                 title: str,
                 lead: str,
                 main_text: list
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
        self.commends = comments
        self.title = title
        self.main_text = main_text
        self.lead = lead

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
        # todo



class _NewsTypes(object):
    CENTRAL_MEDIA = "central media"
    SELF_EMPLOYED_MEDIA = "self-employed media"
    WEB_NEWS_PLATFORM = "web news platform"
