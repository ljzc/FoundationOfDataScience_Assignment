import urllib.request as request


def simple_test():
    response = request.urlopen("http://news.jstv.com")
    html_code = open("html_code.txt", "w")
    html_code.write(response.read().decode("utf-8"))
    html_code.close()


if __name__ == '__main__':
    simple_test()