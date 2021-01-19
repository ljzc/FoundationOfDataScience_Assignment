from bs4 import BeautifulSoup

_HTML = "html"
_BODY = "body"
_H1 = "h1"
_H2 = "h2"
_H3 = "h3"
_DIV = "div"
_P = "p"
_A = "a"
_BR = "br"
_HR = "hr"
_LI = "li"
_STRONG = "strong"


class Tag:

    def __init__(self, tag, text="", **kwargs):
        self.tag = tag
        self.kwargs = kwargs
        self.text = text
        self.content = []

    def add(self, tag):
        self.content.append(tag)
        return self

    def get_begin_tag(self):
        if(self.tag == _HR or self == _BR):
            return "<{tag} />".format(tag=self.tag)
        begin_tag = "<" + self.tag
        if (self.kwargs != None):
            for it in self.kwargs.items():
                begin_tag += " {0}=\"{1}\"".format(it[0], it[1])
        begin_tag += ">"
        return begin_tag

    def get_end_tag(self):
        if (self.tag == _HR or self == _BR):
            return ""
        return "</{0}>".format(self.tag)

    def inner_to_string(self):
        html = self.get_begin_tag()
        for tag in self.content:
            html += tag.inner_to_string()
        if self.text != "":
            html += self.text
        html += self.get_end_tag()
        return html

    def to_html_string(self):
        soup = BeautifulSoup(self.inner_to_string(), 'lxml')
        return soup.prettify()


def html():
    return Tag(_HTML)


def body():
    return Tag(_BODY)


def h1(text, id_no="default h1"):
    return Tag(_H1, text=text, **{"id": id_no})


def h2(text, id_no="default h2"):
    return Tag(_H2, text=text, **{"id": id_no})


def h3(text, id_no="default h3"):
    return Tag(_H3, text=text, **{"id": id_no})


def div(text="", id_no="default div"):
    return Tag(_DIV, text=text, **{"id": id_no})


def p(text="", id_no="default p"):
    return Tag(_P, text=text, **{"id": id_no})


def a(text="", href=""):
    if text == "":
        text = href
    return Tag(_A, text=text, **{"href": href})


def li(text="", id_no="default li"):
    return Tag(_LI, text=text, id_no=id_no)


def strong(text="default text"):
    return Tag(_STRONG, text=text)

def hr():
    return Tag(_HR)
