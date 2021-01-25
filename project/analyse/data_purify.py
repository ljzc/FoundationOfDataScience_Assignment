import crawler.src.util.util as util
from crawler.src.news.news import News
from analyse.analyse_util import news_from_local_file


def flit(src_dir: str, dest_dir: str, rule):
    src_news = news_from_local_file(src_dir)
    for name, raw_news in src_news:
        if rule(raw_news):
            f = open(f"{dest_dir}\\{name}", 'w', encoding='utf-8')
            f.write(raw_news.to_string())
            f.close()


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

keywords_of_taeget_news = [
    '新冠', '疫', '确诊', '病例', '医', '患者', '病人',
    '急诊', '防护服', '肺炎', '防控', '感染', '预防', '隔离',
    '武汉', '核酸检测'

]


if __name__ == '__main__':
    flit("D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\weibo_data",
         "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\filted",
         lambda n: keywords_in_news(n, keywords_of_taeget_news))
