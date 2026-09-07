import re
import csv
from collections import Counter

import jieba

STOP_WORDS = set()
with open("./data/stop_words.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        STOP_WORDS.add(line.strip())


def clean_text(raw_text):
#这个函数任务：拿到原始字符串raw_text，依次做三件清洗工作
# 1. 把文本里面所有网址（http开头）删掉，用re.sub
# 2. 删掉表情、奇怪符号，只保留中文、英文、数字、空格
# 3. 把多个连续换行/空格合并成单个空格，最后去掉两端空白

  raw_text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', raw_text)
  raw_text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9\s]', '', raw_text)
  #  [] ：字符集合
  #  ^  写在 [] 里面代表取反：匹配不在这个集合里的字符
  #  \u4e00-\u9fa5 ：Unicode里所有中文字符范围
  #  a-zA-Z ：大小写英文字母
  #  0-9 ：数字
  #  \s ：空白字符（空格、换行、tab）
 
  raw_text = re.sub(r'\s+', ' ', raw_text)
  return raw_text.strip()


def filter_stop_words(word_list):
  #这个函数任务：拿到一个词列表word_list，返回一个新列表，
  # 里面的词都不是停用词

    return [word for word in word_list if word not in STOP_WORDS]


def count_word_frequency(word_list):
   #传入过滤完的词语列表，统计每个词出现多少次，返回统计结果。
   
    return dict(Counter(word_list))


def read_text_file(file_path):
    #读取data文件夹中的txt文本文件，返回文件内容字符串
    with open (file_path, mode = "r", encoding = "utf-8") as f:
        return f.read()


def save_word_frequency_to_csv(freq_dict,save_path):
    #将统计完成的词频字典freq_dict保存到csv文件中，文件路径为save_path
    #csv两列：单词，频次
    with open(save_path, mode = "w", encoding = "utf-8", newline='') as f:
        #不加newline=''会出现空行，用csv就带上newline=''
        writer = csv.writer(f)
        #写入表头
        writer.writerow(["单词", "频次"])
        #循环遍历字典，写入每一行
        for word, cnt in freq_dict.items():
            writer.writerow([word, cnt])

if __name__ == "__main__":
    #设置输入输出文件路径
    input_file = "./data/test.txt"
    output_file = "./result/word_frequency.csv"

    #读取文本文件
    raw_text = read_text_file(input_file)
    #清洗文本
    clean_text_str = clean_text(raw_text)
    #使用jieba进行分词，得到词列表
    word_list = [w for w in jieba.cut(clean_text_str) if w.strip()]
    #过滤停用词
    filtered_words = filter_stop_words(word_list)
    #统计词频
    word_freq = count_word_frequency(filtered_words)
    #保存到csv文件
    save_word_frequency_to_csv(word_freq, output_file)

    print(f"词频统计完成，结果已保存到 {output_file}")

