"""doctring"""
# coding=utf-8

import os
import sys
from zhon.hanzi import punctuation
import re
from . import getConfig
import jieba
# 用jieba分词

# 读取配置
gConfig = {}
gConfig = getConfig.get_config('seq2seq.ini')
conv_path = gConfig['resource_data']

if not os.path.exists(conv_path):
    print('No resource data here')
    sys.exit()

# 识别读取训练集的数据并存入一个List中,分三步:
#  1.打开文件
#  2.读取文件中的内容，并对文件的数据进行初步处理
#  3.找出我们想要的数据存储下来
convs = []  # 用于存储对话的列表
with open(conv_path, encoding='utf-8') as f:
    one_conv = []        # 存储一次完整对话
    for line in f:
        # 去除换行符，并将原文件中已经分词的标记去掉，重新用jieba分词.
        line = line.strip('\n').replace('?', '')
        line = re.sub(r"[%s]+" % punctuation, "", line)
        if line == '':
            continue
        if line[0] == gConfig['e']:
            if one_conv:
                convs.append(one_conv)
            one_conv = []
        elif line[0] == gConfig['m']:
            one_conv.append(line.split(' ')[1])  # 将一次完整的对话存储下来
#  接下来，我们需要对训练集的对话进行分类，分为问和答，或者叫上文、下文，这个主要是作为encoder和decoder的熟练数据
#  我们一般分为以下几个步骤
#   1、初始化变量，ask response为List
#   2、按照语句的顺序来分为问句和答句，根据行数的奇偶性来判断
#   3、在存储语句的时候对语句使用结巴分词，jieba.cut

# 把对话分成问与答两个部分
seq = []
for conv in convs:
    if len(conv) == 1:
        continue
    if len(conv) % 2 != 0:  # 因为默认是一问一答的，所以需要进行数据的粗裁剪，对话行数要是偶数的
        conv = conv[:-1]
    for i in range(len(conv)):
        if i % 2 == 0:
            conv[i] = " ".join(jieba.cut(conv[i]))  # 使用jieba分词器进行分词
            conv[i+1] = " ".join(jieba.cut(conv[i+1]))
            # 因为i是从0开始的，因此偶数行为发问的语句，奇数行为回答的语句
            seq.append(conv[i]+'\t'+conv[i+1])

seq_train = open(gConfig['seq_data'], 'w', encoding='utf-8')

for i in range(len(seq)):
    seq_train.write(seq[i]+'\n')

    if i % 1000 == 0:
        print(len(range(len(seq))), '处理进度：', i)

seq_train.close()
