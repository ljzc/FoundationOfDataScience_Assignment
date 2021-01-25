import numpy as np
import matplotlib.pyplot as plt
from analyse.analyse_util import bins_of, normal, filter_np, chi_square_test, get_dict
import math
from matplotlib import font_manager
from scipy.stats import probplot

def hist_of_1(file_name: str):
    comment = np.loadtxt(file_name, delimiter=", ", skiprows=1, usecols=(2,), unpack=True, encoding='utf-8')
    comment = filter_np(lambda a: a < 10000, comment)
    # comment = np.log(comment)
    plt.hist(comment, density=True, range=(0, 12), bins=bins_of(comment, 10, 20))

    mu = np.average(comment)
    sigma = np.std(comment, ddof=1)
    # norm = np.random.normal(mu, sigma, 10000)
    # plt.hist(comment, density=True, range=(0, 12), bins = bins_of(norm, 10, 0.2))
    x = np.arange(0, 5000, 0.001)
    density = normal(x, mu, sigma ** 2)
    print(density)
    plt.plot(x, density)
    plt.xlim(0, 5000)
    my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/STSONG.TTF")
    plt.xlabel("新闻数量", fontproperties=my_font, fontsize= 10)

    plt.ylabel("频率",fontproperties=my_font, fontsize= 10)
    plt.title("原始评论数量分布", fontproperties=my_font, fontsize= 15)
    plt.savefig("未经处理的新闻评论数量分布.jpeg", dpi=500)
    plt.show()
    # print(chi_square_test(bins_of(comment, 20, 0.1), mu, sigma, comment))
    # print(chi_square_test(bins_of(list(norm.tolist()), 20, 0.1), mu, sigma, norm))

def hist_of_2(file_name: str):
    comment = np.loadtxt(file_name, delimiter=", ", skiprows=1, usecols=(2,), unpack=True, encoding='utf-8')
    comment = filter_np(lambda a: a < 10000, comment)
    # comment = np.log(comment)
    plt.hist(comment, density=True, range=(0, 12), bins=bins_of(comment, 10, 20))

    mu = np.average(comment)
    sigma = np.std(comment, ddof=1)
    # norm = np.random.normal(mu, sigma, 10000)
    # plt.hist(comment, density=True, range=(0, 12), bins = bins_of(norm, 10, 0.2))
    x = np.arange(0, 5000, 0.001)
    density = normal(x, mu, sigma ** 2)
    print(density)
    plt.plot(x, density)
    plt.xlim(0, 5000)
    # plt.xlabel("新闻数量")
    # plt.ylabel("频率")
    plt.savefig("舍弃1000+.jpeg", dpi=1000)
    plt.show()
    # print(chi_square_test(bins_of(comment, 20, 0.1), mu, sigma, comment))
    # print(chi_square_test(bins_of(list(norm.tolist()), 20, 0.1), mu, sigma, norm))

def hist_of_3(file_name: str):
    comment = np.loadtxt(file_name, delimiter=", ", skiprows=1, usecols=(2,), unpack=True, encoding='utf-8')
    # comment = filter_np(lambda a: a < 6000, comment)
    comment = np.log10(comment)
    plt.hist(comment, density=True, range=(0, 5), bins=bins_of(comment, 10, 0.1))

    mu = np.average(comment)
    sigma = np.std(comment, ddof=1)
    # norm = np.random.normal(mu, sigma, 10000)
    # plt.hist(comment, density=True, range=(0, 12), bins = bins_of(norm, 10, 0.2))
    x = np.arange(0, 12, 0.001)
    density = normal(x, mu, sigma ** 2)
    print(density)
    plt.plot(x, density)
    plt.xlim(0, 5)
    my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/STSONG.TTF")
    plt.xlabel("新闻数量的对数", fontproperties=my_font, fontsize=10)

    plt.ylabel('密度', fontproperties=my_font, fontsize=10)
    plt.title("对数处理评论数量分布", fontproperties=my_font, fontsize=15)
    plt.savefig("对数处理的新闻评论数量分布.jpeg", dpi=500)
    plt.show()
    print(chi_square_test(bins_of(comment, 20, 0.1), mu, sigma, comment), mu, sigma)
    # print(chi_square_test(bins_of(list(norm.tolist()), 20, 0.1), mu, sigma, norm))


def hist_of(file_name: str):
    comment = np.loadtxt(file_name, delimiter=", ", skiprows=1, usecols=(2,), unpack=True, encoding='utf-8')
    part_1 = filter_np(lambda a: a < 1000, comment)
    part_2 = filter_np(lambda a: a > 999, comment)
    part_1 = np.log(part_1)

    comment = np.append(part_1, part_2)
    comment = np.log(comment)
    plt.hist(comment, density=True, range=(0, 5), bins=bins_of(comment, 10, 0.05))

    mu = np.average(comment)
    sigma = np.std(comment, ddof=1)
    norm = np.random.normal(mu, sigma, 10000)
    # plt.hist(comment, density=True, range=(0, 12), bins = bins_of(norm, 10, 0.2))
    x = np.arange(0, 5000, 0.001)
    density = normal(x, mu, sigma ** 2)
    print(density)
    plt.plot(x, density)
    plt.xlim(0, 5000)
    plt.xlabel("新闻数量")
    plt.ylabel("密度")
    plt.savefig("hist.jpeg", dpi=1000)
    plt.show()
    print(chi_square_test(bins_of(comment, 20, 0.1), mu, sigma, comment))
    print(chi_square_test(bins_of(list(norm.tolist()), 20, 0.1), mu, sigma, norm))


def prob(file_name):
    comment = np.loadtxt(file_name, delimiter=", ", skiprows=1, usecols=(2,), unpack=True, encoding='utf-8')
    # comment = filter_np(lambda a: a < 6000, comment)
    comment = np.log(comment)
    probplot(comment, plot=plt)
    plt.savefig("原始数据的Q-Q图.jpeg", dpi=700)
    plt.show()



from analyse.analyse_util import create_mind_frequency
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def mind_fig():

    # 生成横纵坐标信息
    mind_dict = get_dict(
        "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\mind_dictionary\\第四次迭代结果（100~120）.txt")
    res = create_mind_frequency(
        "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\comment_bnt\\all",
        mind_dict)

    dates = sorted(list(res[list(mind_dict.keys())[0]].keys()))
    xs = dates
    ys = {}
    my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/STSONG.TTF")
    for key in mind_dict.keys():
        ys[key] = []
    for date in dates:
        for key in mind_dict.keys():
            ys[key].append(res[key][date])
    for key in mind_dict.keys():
        # 配置横坐标
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        # Plot
        plt.plot(xs, ys[key], label=key)
        plt.legend(loc="upper right")
        plt.gcf().autofmt_xdate()  # 自动旋转日期标记
        plt.savefig(f"{key}_变化趋势.jpeg")
        plt.show()
        plt.close()



if __name__ == '__main__':
    # hist_of_3(
    #     "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\2021-01-23 18-56-28微博转赞评论(11842).csv")
    # # hist_of_2(
    # #     "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\2021-01-22 11-32-18微博转赞评论(8314).csv")
    # # hist_of_3(
    # #     "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\2021-01-22 11-32-18微博转赞评论(8314).csv")
    mind_fig()