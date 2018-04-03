import re
import csv
import time
import numpy
import os
import requests
from bs4 import BeautifulSoup
from collections import deque


path = '/Users/trevor/Documents/Codes/jieba/comment.csv'
csvFile = open(path,'a+',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
writer.writerow(('id', 'name'))

URL = 'http://guba.eastmoney.com/news,cjpl,750416430_{page}.html#storeply'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


def create_request(url, headers, page):
    url = url.format(page=page)
    resp = requests.get(url, headers=headers, allow_redirects=False).text
    bsObj = BeautifulSoup(resp, 'html.parser')
    result = bsObj.find_all(id="zwlist") # preprocess html file
    str_result = str(result[0]) # change the txt file to string type

    return str_result


def get_ID(str_result):
    id = re.compile(r'<span class="influence" data-uid="(\d+)"></span>') #re
    ID_list = id.findall(str_result)

    return ID_list


def get_comment(str_result):
    comment = re.compile(r'<div class="zwlitext stockcodec">((?:.|\n)*?)</div>')
    list = comment.findall(str_result)
    comment_list=[]
    for i in range(len(list)):
        comment = ''.join(re.findall(r'[\u4e00-\u9fa5_A-Z0-9]', list[i])) # only keep Chinese, English Upper word and Numbers
        comment_list.append(comment)

    return comment_list


def output_result(page):
    for p in range(1, page + 1):
        req = create_request(URL, headers, p)
        id_list = get_ID(req)
        comment_list = get_comment(req)
        for i in range(len(id_list)):
            Content = (id_list[i], comment_list[i])
            writer.writerow(Content)
            print(Content)


output_result(page=15)

csvFile.close()
