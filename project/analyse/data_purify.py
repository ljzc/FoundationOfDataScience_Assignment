import crawler.src.util.util as util
from crawler.src.news.news import News


def flit(src_dir: str, dest_dir: str, rule):
    src_news = util.news_from_local_file(src_dir)
    for raw_news in src_news:
        if rule(raw_news):
            util.to_mark_down(raw_news.to_string(), dest_dir,
                              "{time}_{title}".format(time=raw_news.time.strftime("%Y-%m-%d"),
                                                      title=util.beautify(raw_news.title)))


def keywords_in_news(news: News, keywords: list):
    for keyword in keywords:
        if (keyword in news.title) or (keyword in news.lead) or (keyword in news.main_text):
            return True
    return False


def comment_more_then(news: News, minimal: int):
    r"""

    :param news:
    :param minimal: 评论数量的标准
    :return: 评论数量小于minimal的新闻返回false
    """
    return news.comment_num() >= minimal
