import re


def test_re():
    # print(re.match("转发\\[([0-9]+)\\]", "转发[100]")[1])
    print(re.match('(\\S+ \\S+).*?', "02月03日 10:21 来自网页")[1])
