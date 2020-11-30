from src.util import util


def test_detect_encoding():
    encoding = util.detect_encoding("http://news.jstv.com/a/20201129/1606629502561.shtml")
    assert encoding == "utf-8"

