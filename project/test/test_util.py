from crawler.src.util import util


def test_get_code_of_rendered_page():
    code = util.get_code_of_rendered_page("https://finance.sina.com.cn/chanjing/2020-12-03/doc-iiznezxs4950037.shtml")
    print(code)
    assert True
