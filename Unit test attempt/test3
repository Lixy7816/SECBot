

#coding=utf-8　
import json
import unittest
from views import unit_chat
import requests
import random


from views import chat
class Chat_test(unittest.TestCase):
    def test_chat(self):

        test_str = chat(' ')
        # 如果接受到的内容为空，则给出相应的回复
        self.assertEqual(test_str, '不好意思，我们正在学习，稍后再回复您。')
        test_str2= chat( '')
        self.assertEqual(test_str2, '不好意思，我们正在学习，稍后再回复您。')
unittest.main()

