import numpy as np
import matplotlib.pyplot as plt
from analyse.analyse_util import bins_of, normal, filter_np,chi_square_test
import math





def hist_of(file_name: str):
    comment = np.loadtxt(file_name, delimiter=", ", skiprows=1, usecols=(2,), unpack=True, encoding='utf-8')
    comment = filter_np(lambda a: a < 1000, comment)
    comment = np.log(comment)
    bins = plt.hist(comment, density=True, range=(0, 12), bins=bins_of(comment, 10, 0.2))

    mu = np.average(comment)
    sigma = np.std(comment, ddof=1)
    norm = np.random.normal(mu, sigma, 10000)
    plt.hist(comment, density=True, range=(0, 12), bins = bins_of(norm, 10, 0.2))
    x = np.arange(0, 12, 0.001)
    density = normal(x, mu, sigma ** 2)
    print(density)
    plt.plot(x, density)
    plt.xlim(0, 12)
    plt.savefig("hist.jpeg", dpi=1000)
    plt.show()
    print(chi_square_test(bins_of(comment, 20, 0.1), mu, sigma, comment))
    print(chi_square_test(bins_of(list(norm.tolist()), 20, 0.1), mu, sigma, norm))





if __name__ == '__main__':
    hist_of(
        "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\2021-01-22 11-32-18微博转赞评论(8314).csv")
