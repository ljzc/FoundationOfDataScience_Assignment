import datetime
from src.news.comment import Comment, Comments


class News(object):

    '''
    将一个由to_string()方法格式化的字符串解析成一个News对象，返回该对象
    '''
    @staticmethod
    def parse(news_info):
        pass

    def __init__(self,
                 time: datetime.date,
                 author: str,
                 location: str,  # 尽量在导语中选取描述地理位置的词语，如果实在有困难可以先忽略这个，之后用自然语言处理来做
                 news_type: str,  # 使用_NewsTypes类中定义的常量
                 comments: Comments,  # 新闻的评论
                 title: str,
                 lead: str,  # 新闻导语 请将导语从新闻中剔除
                 main_text: str  # 新闻主体部分
                 ):
        # 保证新闻类型来自预先定义好的常量
        assert news_type == _NewsTypes.CENTRAL_MEDIA \
               or news_type == _NewsTypes.SELF_EMPLOYED_MEDIA \
               or news_type == _NewsTypes.WEB_NEWS_PLATFORM

        self.time = time
        self.author = author
        self.location = location
        self.news_type = news_type
        self.commends = comments
        self.title = title
        self.main_text = main_text
        self.lead = lead

        self.emotional_words = dict()
        self.emotional_vector = []
        self.is_significant = False
        self.summery = None
        self.event_type = ""

    '''
    将新闻格式化为一个字符串，以便于写入文件中
    '''
    def to_string(self):
        pass


class _NewsTypes(object):
    CENTRAL_MEDIA = "central media"
    SELF_EMPLOYED_MEDIA = "self-employed media"
    WEB_NEWS_PLATFORM = "web news platform"
