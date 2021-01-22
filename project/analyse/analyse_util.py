import os
from datetime import datetime
from crawler.src.news.news import parse_from_info
import re
from numpy import ndarray
import math
import numpy as np
from scipy.stats import norm, chi2


def attrs_file_of_news_set(news_set):
    attrs_infos = ['转发, 赞, 评论\n']
    for news in news_set:
        attrs_infos.append(f"{news.attrs['repost']}, {news.attrs['attitude']}, {news.attrs['comment_number']}\n")
    f = open(f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}微博转赞评论({len(attrs_infos)}).csv", 'w', encoding='utf-8')
    f.writelines(attrs_infos)
    f.close()


def news_from_local_file(path: str):
    files = []
    for file_name in os.listdir(path):
        files.append(f"{path}\\{file_name}")
    for file in files:
        f = open(file, "r", encoding="utf-8")
        temp = parse_from_info(f.read())
        f.close()
        yield temp


def purify_sentence(sentence: str):
    segments = re.split(
        '[\u3002\uff1f\uff01\uff0c\u3001\uff1b\uff1a\u201c\u201d\u2018\u2019\uff08\uff09\u300a\u300b\u3008\u3009\u3010\u3011\u300e\u300f\u300c\u300d\ufe43\ufe44\u3014\u3015\u2026\u2014\uff5e\ufe4f\uffe5]',
        sentence)
    pure_sentence = ''
    for segment in segments:
        pure_sentence = pure_sentence + " " + segment
    return pure_sentence


def bins_of(data: list, minimal_amount: int, interval):
    data.sort()
    bins = []
    freq = []
    idx = 0
    low = min(data)
    while low <= max(data):
        frequency = 0
        while idx < len(data) and data[idx] < low + interval:
            frequency += 1
            idx += 1
        freq.append(frequency)
        low += interval
    range_no = 0
    bins.append(range_no * interval + min(data))
    while range_no < len(freq):
        accumulate_amount = 0

        while accumulate_amount < minimal_amount and range_no < len(freq):
            accumulate_amount += freq[range_no]
            range_no += 1
        # print(f"(~{range_no * interval + math.floor(min(data))}) : {accumulate_amount}")
        bins.append(range_no * interval + min(data))
    return bins


def find_left_out(urls_dir, news_dir):
    url_set = set()
    for file_name in os.listdir(urls_dir):
        f = open(f"{urls_dir}\\{file_name}", 'r', encoding='utf-8')
        for url in f.read().split("\n"):
            if re.match("^https.+", url):
                url_set.add(url)
        f.close()

    for local_news in news_from_local_file(news_dir):
        if local_news.src in url_set:
            url_set.remove(local_news.src)
    f = open("../result_1.txt", 'a', encoding='utf-8')
    for url in url_set:
        f.write(url + '\n')
    f.close()


def normal(x, mu, sigma_sqr):
    temp1 = (1 / math.sqrt(2 * np.pi * sigma_sqr))
    print(temp1)
    temp2 = np.exp(0 - ((x - mu) * (x - mu) / (2 * sigma_sqr)))
    print(temp2)
    return temp1 * temp2


def central_moment(data, n):
    r"""
    计算n阶中心距
    :param data: 数据
    :param n: 阶数
    :return:
    """
    mu = np.average(data)
    return np.average((data - mu) ** n)


def filter_np(rule, data):
    judge = []
    for num in data:
        judge.append(rule(num))
    return data[judge]


def chi_square_test(bins, mu, sigma, data):
    # 标准化
    n = len(data)
    data = (data - mu) / sigma
    data = np.sort(data)
    bins = (np.array(bins) - mu ) / sigma

    # 经验频数
    exp = []
    idx = 0
    for i in range(0, len(bins) - 1):
        freq = 0
        while idx < len(data) and data[idx] < bins[i + 1]:
            freq += 1
            idx += 1
        exp.append(freq)
    exp = np.array(exp)

    # 理论频数
    theory = []
    for i in range(1, len(bins)):
        theory.append((norm.cdf(bins[i]) - norm.cdf(bins[i - 1])) * n)
    # theory[0] = norm.cdf(bins[1]) * n
    # theory[-1] += (1 - norm.cdf(bins[-1])) * n
    theory = np.array(theory)

    for i in range(0, len(theory)):
        print(f"{exp[i]}    {theory[i]}")
    # 计算统计量
    T = np.sum(np.square(exp - theory) / theory)

    # 检验
    p = chi2.cdf(T, len(bins) - 1 - 2 - 1)
    # p = chi2.cdf(7.962, 16)
    print(f"统计量值：          {T}\n"
          f"假设成立的最小置信度： {p}")


if __name__ == '__main__':
    # attrs_file_of_news_set(news_from_local_file('C:\\Users\\ljzc\\Desktop\\新建文件夹'))
    # comment = np.loadtxt(
    #     'D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\2021-01-22 11-32-18微博转赞评论(8314).csv',
    #     delimiter=", ", skiprows=1, usecols=(2,), unpack=True, encoding='utf-8')
    # comment = filter_np(lambda a: a < 1000, comment)
    # comment = np.log(comment)
    #
    # chi_square_test(bins_of(comment, 10, 0.1), np.average(comment), np.std(comment, ddof=1), comment)
    # print(central_moment(comment, 3) / ((np.std(comment, ddof=1)) ** 3))
    # print(np.max(comment))
    # find_left_out('D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\resorce_2', 'C:\\Users\\ljzc\\Desktop\\微博数据集')
    # data = np.random.randn(9000)
    # chi_square_test(bins_of(data, 10, 0.1), np.average(data), np.std(data,ddof=1), data)
    for news in news_from_local_file('D:\OneDrive\文档\大二上\数据科学基础大作业\FoundationOfDataScience_Assignment\project\weibo_data'):
        news.comments