from crawler.src.util.html_constructor import *
def test_tag():
    h_1 = h1("测试标题h1", id_no="测试标题h1_id")

    h_2 = h2("测试标题h2", id_no="测试标题h2_id")

    link = a("测试链接","https://cn.bing.com/")

    i1 = li("测试列表",id_no="测试列表id")

    l2 = li("测试列表2",id_no="测试列表2")

    p_ = p("测试段落", id_no="测试段落").add(link)

    dv = div("测试分块", id_no="测试分块id").add(i1).add(l2)

    body_ = body().add(h_1).add(h_2).add(p_).add(dv)

    ht = html().add(body_)

    f = open("test.md", "w", encoding="utf-8")

    f.write(ht.to_html_string())

    f.close()

