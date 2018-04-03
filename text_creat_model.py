import re
import numpy
import jieba
from jieba import posseg
from gensim.models import Word2Vec
from gensim.models import KeyedVectors


class MySentence(object):
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            for line in f.readlines():  # 依次读取每行
                line = line.strip()  # 去掉每行头尾空白
                if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
                    continue  # 是的话，跳过不处理
                chinesesentence = line.split(",", 1)[1] # 只保留tuple第二个元素
                wordlist = jieba.lcut(chinesesentence)

                yield wordlist


Sentences = MySentence(filename=r'/Users/trevor/Documents/Codes/jieba/comment.csv')

# 训练模型，得到词组的向量表示

model = Word2Vec(sentences=Sentences, size=100, window=5, min_count=5, workers=4)

model.wv.save_word2vec_format(fname=r'/Users/trevor/Documents/Codes/jieba/text_word2vec_binary.bin', binary=True)
