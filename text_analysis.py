import re
import numpy
import jieba
from jieba import posseg
from gensim.models import Word2Vec
from gensim.models import KeyedVectors


model = KeyedVectors.load_word2vec_format(r'/Users/trevor/Documents/Codes/jieba/text_word2vec_binary.bin', binary=True)
print(len(model.vocab))
print(model['股市'])
print(model.similarity('股市', '茅台'))
