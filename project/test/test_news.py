from crawler.src.news.news import News
from crawler.src.news.news import _NewsTypes
from crawler.src.news.comment import *
from datetime import date


def test_news_to_string():

    f = open("news_info\\" + datetime.datetime.now().strftime("(%Y-%m-%d)") + ".md", "w", encoding="utf_8").write(News(
        date.today(),
        "测试作者",
        "https://cn.bing.com/",
        False,
        "测试地址，这部分可能被改动，",
        _NewsTypes.WEB_NEWS_PLATFORM,
        Comments().add_comment(Comment(date.today(), "测试评论1", "测试评论作者1"))
            .add_comment(Comment(date.today(), "测试评论2", "测试评论作者2")),
        "测试新闻标题",
        "测试新闻导语测试新闻导语测试新闻导语测试新闻导语测试新闻导语测试新闻导语测试新闻导语测试新闻导语测试新闻导语",
        ["测试新闻正文段1测试新闻正文段1测试新闻正文段1测试新闻正文段1测试新闻正文段1测试新闻正文段1", "段2", "段3"]
    ).to_string())
