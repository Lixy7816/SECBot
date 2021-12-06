
# coding = utf-8
from . import execute
import jieba

#"""定义应答函数，用于获取输入信息并返回相应的答案"""
def botReply(input):
    req_msg=" ".join(jieba.cut(input))
    res_msg = execute.predict(req_msg)
    
    res_msg = res_msg.replace('_UNK', '^_^')
    res_msg=res_msg.strip()

    # 如果接受到的内容为空，则给出相应的回复
    if res_msg == ' ':
      res_msg = '请与我聊聊天吧'
    print(res_msg)
    return res_msg