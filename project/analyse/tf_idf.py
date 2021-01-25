r"""
逆文本频率求解
"""
from gensim.models.tfidfmodel import TfidfModel
from gensim import corpora
import os

dir_path_1 = "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\comment_bnt"
dir_path = ""

def tf_idf(texts):
    dictionary = corpora.Dictionary(texts)
    re_dict = {}
    for key in dictionary.keys():
        re_dict[dictionary[key]] = key
    corpus = [dictionary.doc2bow(text) for text in texts]
    tf_idf_model = TfidfModel(corpus, normalize=False)
    word_tf_tdf = list(tf_idf_model[corpus])
    # print('词典:', dictionary.token2id)
    # print('词频:', corpus)
    segment_cnt = 0
    for segment_it in word_tf_tdf:
        f = open(f"{dir_path}\\segment_{segment_cnt}.csv", "a", encoding="utf-8")
        print("segment: ", segment_cnt)
        segment_cnt += 1
        for word_it in sorted(segment_it, key=lambda w : w[1]):
            f.write(f"{dictionary[word_it[0]]},{word_it[1]}\n")
        f.close()


def get_texts(dir_path):
    texts = []
    names = []
    for name in os.listdir(dir_path):
        f = open(f"{dir_path}\\{name}", "r", encoding="utf-8")
        texts.append(" ".join(f.read().split("\n")).split(" "))
        names.append(name)
    return names, texts


if __name__ == '__main__':
    for sub_dir in os.listdir(dir_path_1):
        dir_path = f"{dir_path_1}\\{sub_dir}"
        tf_idf(get_texts(dir_path))