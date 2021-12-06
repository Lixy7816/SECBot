
# coding = utf-8
from . import execute
import jieba

#"""定义应答函数，用于获取输入信息并返回相应的答案"""
def botReply(input):
    req_msg=" ".join(jieba.cut(input))
    res_msg = execute.predict(req_msg)
    
    res_msg = res_msg.replace('_UNK', '^_^')
    res_msg=res_msg.strip()
    return res_msg