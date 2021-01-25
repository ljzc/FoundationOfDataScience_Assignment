r"""
语料库构建模块
"""
import jieba
from analyse.analyse_util import news_from_local_file
import re
import datetime
import os
def construct_bnc_comment(dir_path, dest_dir):
    comments_dict = {}
    for name, news in news_from_local_file(dir_path):
        for comment in news.comments.comments:
            if comment.time in comments_dict:
                comments_dict[comment.time].append(comment)
            else:
                comments_dict[comment.time] = [comment,]
    for time in comments_dict.keys():
        f = open(f'{dest_dir}//{time.strftime("%Y-%m-%d")}.txt', "a", encoding='utf-8')
        for comment in comments_dict[time]:
            lines = []
            for sentence in break_by_sentence(purify_comment(comment.content.strip())):
                lines.append("\n".join(cut_into_sort_sentence(sentence)))
            f.write("\n".join(lines) + "\n")
        f.close()

def putify_all_bnc_in(dir_path):
    for name in os.listdir(dir_path):
        print(f"正在处理：{dir_path}\\{name}")
        f = open(f"{dir_path}\\{name}", "r", encoding='utf-8')
        result = "\n".join(re.split("\n+", f.read()))
        f.close()
        f = open(f"{dir_path}\\{name}", "w", encoding='utf-8')
        f.write(result)






def construct_bnc(dir_path):
    f = open("bnc.txt", 'a', encoding='utf-8')
    for name, news in news_from_local_file(dir_path):
        sentences = []
        temp = [break_by_sentence(news.lead.strip())]
        for text in news.main_text:
            temp.append(break_by_sentence(text))
        for comment in news.comments.comments:
            temp.append(break_by_sentence(purify_comment((comment.content.strip()))))
        for group in temp:
            for sentence in group:
                sentences += cut_into_sort_sentence(sentence)
        result = []
        for i in range(0, len(sentences)):
            if sentences[i] != '':
                result.append(sentences[i].strip().replace("\n", ""))

        f.write("\n".join(result)+"\n")
    f.close()

def purify_comment(comment: str):
    result = re.match("(回复[\u0040\uff20].+?[\uff1a\u003a])(.+)", comment)
    if result is not None:
        return result[2]
    else:
        return comment

def break_by_sentence(paragraph: str):
    return re.split('[\uff01\uff0e\uff1f\uff1b]', paragraph)


def purify_sentence(sentence: str):
    segments = re.split(
        '[\u3002\uff1f\uff01\uff03\uff0c\u3001\uff1b\uff3d\uff1a\u201c\u201d\u2018\u2019\uff08\uff09\u300a\u300b'
        '\u3008\u3009\u3010\u3011\u300e\u300f\u300c\u300d\ufe43`~\ufe44\u3014\u3015\uff20\u2026\u2014\u0040\u0023\uff5e\ufe4f\uffe5\u003a\[\].]',
        sentence)
    return "".join(segments)


def cut_into_sort_sentence(long_sentence: str):

    raw_cut = re.split("[\uff1a\u003a\uff0c\u002c]",long_sentence.strip())
    for i in range(0, len(raw_cut)):
        raw_cut[i] = list(jieba.cut(purify_sentence(raw_cut[i])))

    short_sentences = []
    current_len = 0
    idx = 0
    while idx < len(raw_cut):
        temp = []
        while idx < len(raw_cut) and current_len < 5:
            current_len += len(raw_cut[idx])

            temp.append(" ".join(raw_cut[idx]))
            idx += 1
        short_sentences.append(" ".join(temp))
        temp = []
        current_len = 0
    return short_sentences

def combine(dir_path: str):
    for sub_sir in os.listdir(dir_path):
        res = []
        for name in os.listdir(f"{dir_path}\\{sub_sir}"):
            sub_f = open(f"{dir_path}\\{sub_sir}\\{name}", "r", encoding="utf-8")
            res.append(sub_f.read())
            sub_f.close()
        f = open(f"{dir_path}\\{sub_sir}.txt", "w", encoding="utf-8")
        f.writelines(res)
        f.close()



if __name__ == '__main__':
    # f = open("D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\bnc.txt", "r", encoding="utf-8")
    # f_out = open("D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\bnc_2.txt", "a", encoding="utf-8")
    # for line in f.readlines():
    #     line = line.replace("\u0040", "")
    #     line = line.replace("\uff20", "")
    #     line = line.replace("[", "")
    #     line = line.replace("]", "")
    #     line = line.replace("~", "")
    #     line = line.replace("`", "")
    #     line = line.replace("...", "")
    #     line = line.replace("....", "")
    #     line = " ".join(re.split(" +", line))
    #     f_out.write(line.strip().strip(".").strip() + "\n")
    # f.close()
    # f_out.close()
    # print("开始生成语料库")
    # construct_bnc_comment("D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\filted",
    #                       "D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\comment_bnt")
    #
    # print("开始后处理文件")
    # putify_all_bnc_in("D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\comment_bnt")
    combine("D:\\OneDrive\\文档\\大二上\\数据科学基础大作业\\FoundationOfDataScience_Assignment\\project\\analyse\\comment_bnt")