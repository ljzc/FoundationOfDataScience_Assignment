r"""
这个模块用于构建词向量
"""
import gensim
from gensim.models import word2vec, KeyedVectors
from sklearn.decomposition import PCA
from matplotlib import pyplot
import logging
import os


input_dir = "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\comment_bnt_duration"
output_dir = "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\comment_model"




pyplot.rcParams['font.family'] = ['SimHei']
pyplot.rcParams['axes.unicode_minus'] = False

def vector(input, output):
    # 设置输出日志
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                        level=logging.INFO)
    # 读取分词好的文件
    sentences = word2vec.LineSentence(input)
    #  训练模型
    model = gensim.models.Word2Vec(sentences, size=200, min_count=5)
    # 保存
    model.wv.save_word2vec_format(output, binary=True)
    print(model)
    # 图形化表示
    X = model[model.wv.vocab]
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)

    pyplot.scatter(result[:, 0], result[:, 1])
    words = list(model.wv.vocab)
    for i, word in enumerate(words):
        pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
    pyplot.savefig(output.replace(".bin", ".jpeg"), dpi=500)
    pyplot.show()
    return pyplot

def load_vector(path: str):
    print("开始加载")
    model = KeyedVectors.load_word2vec_format(path, binary=True)
    words = list(model.wv.vocab)
    print("words = ", words)
    X = model[model.wv.vocab]
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)

    pyplot.scatter(result[:, 0], result[:, 1])
    words = list(model.wv.vocab)
    for i, word in enumerate(words):
        pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
    pyplot.savefig("总体词库词向量可视化.jpeg", dpi=500)
    pyplot.show()
    return pyplot
    return model

def create_models(in_dir, out_dir):
    for name in os.listdir(in_dir):
        vector(f"{in_dir}\\{name}", f"{out_dir}\\{name.replace('txt', 'bin')}")













if __name__ == '__main__':
    load_vector("D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\comment_model\\embedding.bin")