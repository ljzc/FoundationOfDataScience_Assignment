from crawler.src.news.news import News
from crawler.src.news_parser.lizhi_news_parser import LiZhiNewsParser
from bs4 import BeautifulSoup

def test_lizhi():
    news = LiZhiNewsParser().parse("http://news.jstv.com/a/20201130/1606733984697.shtml")
    print(news.title)
    print(news.src)
    print(news.time)
    print(news.lead)
    print(news.main_text)

def test_filter():
    soup = BeautifulSoup("")