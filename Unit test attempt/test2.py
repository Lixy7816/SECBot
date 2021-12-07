#针对BotBcakend的views做的测试

#coding=utf-8　
import json
import unittest
from views import unit_chat
import requests
import random

class Unit_chat(unittest.TestCase):

    def test_unit_chat1(self):
        "测试接口异常，默认回复"
        unit_chat_str = unit_chat('你好','Z3azDuZsqFG888EubjoR1yOR','lFqdE8jVm6DgCCwjeTEFfehrt0g1322q','S62211','88888')
        self.assertEqual(unit_chat_str,"不好意思，我们正在学习，稍后再回复您。")


    def test_unit_chat2(self):
        "测试接口正常，默认回复"
        unit_chat_str = unit_chat('你好','Z3azDuZsqFG888EubjoR1yOR','lFqdE8jVm6DgCCwjeTEFfehrt0g1322q','S62219','88888')
        url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s" % (
            'Z3azDuZsqFG888EubjoR1yOR', 'lFqdE8jVm6DgCCwjeTEFfehrt0g1322q')
        res = requests.get(url)
        access_token = eval(res.text)["access_token"]
        # 根据 access_token 获取聊天机器人接口数据
        unit_chatbot_url = "https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token=" + access_token
        # 拼装聊天接口对应请求发送数据，主要是填充 query 值
        post_data = {
            "log_id": str(random.random()),
            "request": {
                "query": "你好",
                "user_id":"88888"
                
            },
            "session_id": "",
            "service_id": "service_id",
            "version": "2.0"
        }
        res = requests.post(url=unit_chatbot_url, json=post_data)
        unit_chat_obj = json.loads(res.content)
        self.assertEqual(unit_chat_obj["error_code"] != 0,0)

        def test_unit_chat3(self):
            "测试接口正常，默认回复"
            unit_chat_str = unit_chat('中国的首都是？', 'Z3azDuZsqFG888EubjoR1yOR', 'lFqdE8jVm6DgCCwjeTEFfehrt0g1322q', 'S62219',
                                      '88888')
            self.assertEqual(unit_chat_str, "北京")
        
unittest.main()
