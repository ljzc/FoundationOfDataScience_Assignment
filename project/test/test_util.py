from crawler.src.util import util



def test_get_code_of_rendered_page():
    code = util.get_code_of_rendered_page("https://www.gdtv.cn/article/ba7dd95c04b6f11b2ac51625dfaa1508")
    print(code)
    assert True