import numpy as np
import matplotlib.pyplot as plt
from analyse.analyse_util import bins_of, normal, filter_np
import math





def hist_of(file_name: str):
    comment = np.loadtxt(file_name, delimiter=", ", skiprows=1, usecols=(2,), unpack=True, encoding='utf-8')
    comment = filter_np(lambda a: True, comment)
    comment = np.log(comment)
    plt.hist(comment, density=True, range=(0, 12), bins=100)

    mu = np.average(comment)
    sigma = np.std(comment, ddof=1)
    x = np.arange(0, 12, 0.001)
    density = normal(x, mu, sigma ** 2)
    print(density)
    plt.plot(x, density)
    plt.xlim(0, 12)
    plt.savefig("hist.jpeg", dpi=1000)
    plt.show()





if __name__ == '__main__':
    hist_of(
        "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\2021-01-22 11-32-18微博转赞评论(8314).csv")
