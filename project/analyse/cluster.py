r"""
词向量聚类
"""
print(__doc__)

import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs
from analyse.word_vector_constructor import load_vector
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from itertools import cycle
import os


def cluster(file_name):
    # #############################################################################
    # Generate sample data
    # centers = [[1, 1], [-1, -1], [1, -1]]
    # X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
    model = load_vector(
        f"D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\comment_model\\{file_name}")

    X = model[model.wv.vocab]
    pca = PCA(n_components=2)
    X = pca.fit_transform(X)

    # #############################################################################
    # Compute clustering with MeanShift

    # The following bandwidth can be automatically detected using
    bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    print("number of estimated clusters : %d" % n_clusters_)

    clusters = {}
    clusters.fromkeys(labels_unique)
    words = list(model.wv.vocab)
    for i in range(0, len(labels)):
        if labels[i] not in clusters:
            clusters[labels[i]] = [words[i]]
        else:
            clusters[labels[i]].append(words[i])
    print("聚类结果：")
    f = open(f"{file_name.split('.')[0]}_聚类结果.txt", "a", encoding="utf-8")
    for key in labels_unique:
        f.write(" ".join(clusters[key]) + "\n")
    f.close()

    # #############################################################################
    # Plot result

    plt.figure(1)
    plt.clf()

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]
        plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)
    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.savefig(f"{file_name.split('.')[0]}_聚类结果可视化.jpeg", dpi=500)
    plt.show()


def associate(word: str, model, associate_factor):
    words = list(model.wv.vocab)
    if word not in words:
        return []
    word_vec = model.get_vector(word)
    assert word_vec is not None
    target = model.cosine_similarities(model.get_vector(word), model[model.wv.vocab])


    result = []
    for i in range(0, len(target)):
        if target[i] > associate_factor:
            result.append(words[i])
    return result

def associate_with_limit(limit: tuple, target_word, word_model):
    return inner_associate_result_of(limit, target_word, word_model, (0, 1))

def inner_associate_result_of(limit: tuple, target_word, word_model, similarity: tuple):
    mid = ( similarity[0] + similarity[1] ) / 2
    res = associate(target_word, word_model,mid)
    if similarity[1] - similarity[0] < 0.00001 or limit[0] <= len(res) <= limit[1]:
        return mid, res
    elif len(res) < limit[0]:
        return inner_associate_result_of(limit, target_word, word_model, (similarity[0], mid))
    else:
        return inner_associate_result_of(limit, target_word, word_model, (mid, similarity[1]))




def iterate_by_associating(word_model, mind_dict_dir, target_words_dict_path, limit: tuple):
    f = open(target_words_dict_path, "r", encoding="utf-8")
    mind_types = f.read().split("\n\n")
    target_words_dict = {}
    new_mind_dict = {}
    for type in mind_types:
        type = type.split("：")
        target_words_dict[type[0]] = type[1].split("，")
        new_mind_dict[type[0]] = set()
    for mind_type in target_words_dict.keys():
        result = []
        for target_word in target_words_dict[mind_type]:
            similarity, associate_result = associate_with_limit(limit, target_word, word_model)
            result.append(f"{target_word}({similarity}, {len(associate_result)})：{'，'.join(associate_result)}")
            print(f"词语：{target_word}，相似度下限：{similarity}，关联词数量：{len(associate_result)}")
            for new_word in associate_result:
                new_mind_dict[mind_type].add(target_word)
        f = open(f"{mind_dict_dir}\\{mind_type}.txt", "w", encoding="utf-8")
        f.write("\n\n".join(result))
        f.close()
    return new_mind_dict

# import re
#
# def rebude_mind_dict(src_dir):
#     mind_dict = {}
#     for name in os.listdir():
#         if name.split(".")[1] == 'txt':
#             mind_dict[name.split('.')[0]] = set()
#             f = open(f"{src_dir}\\{name}", "r", encoding="utf-8")
#             for line in f.read().split("\n\n"):
#                 words = re.split("\(.+\)")


if __name__ == '__main__':

    model = load_vector('embedding.bin')
    new_dict = associate(model,
                         f"D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\mind_dictionary",
                         f"D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\mind_dictionary\\第三次迭代结果（100~120）.txt",
                         (100, 120))
    #print(associate_with_limit((10, 15), "好开心", model))
    n_mind_dict = []
    amount = 0
    for key in new_dict.keys():
        n_mind_dict.append(f"{key}：{'，'.join(list(new_dict[key]))}")
        amount += len(new_dict[key])
    f = open("第四次迭代结果（100~120）.txt", "w", encoding="utf-8")
    f.write("\n\n".join(n_mind_dict))
    f.close()
    print(amount)


