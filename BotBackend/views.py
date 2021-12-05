# Create your views here.
import json
import random
import requests
from django.shortcuts import HttpResponse

# 根据用户需求选择不同的AI进行回复
# AI依次是:闲聊,诗词,问答,影视
client_ids = ["Z3azDuZsqFG888EubjoR1yOR","Z3azDuZsqFG888EubjoR1yOR","Z3azDuZsqFG888EubjoR1yOR","Z3azDuZsqFG888EubjoR1yOR"]
client_secrets = ["lFqdE8jVm6DgCCwjeTEFfehrt0g1322q","lFqdE8jVm6DgCCwjeTEFfehrt0g1322q","lFqdE8jVm6DgCCwjeTEFfehrt0g1322q","lFqdE8jVm6DgCCwjeTEFfehrt0g1322q"]
service_ids = ["S62219","S62529","S62531","S62530"]
def unit_chat(chat_input, client_id, client_secret, service_id, user_id="88888"):
    """
    description:调用百度UNIT接口，回复聊天内容
    Parameters
      ----------
      chat_input : str
          用户发送天内容
      user_id : str
          发起聊天用户ID，可任意定义
    Return
      ----------
      返回unit回复内容
    """
    # 设置默认回复内容,  一旦接口出现异常, 回复该内容
    chat_reply = "不好意思，俺们正在学习中，随后回复你。"
    # 根据 client_id 与 client_secret 获取access_token
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s" % (
    client_id, client_secret)
    res = requests.get(url)
    access_token = eval(res.text)["access_token"]
    # 根据 access_token 获取聊天机器人接口数据
    unit_chatbot_url = "https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token=" + access_token
    # 拼装聊天接口对应请求发送数据，主要是填充 query 值
    post_data = {
                "log_id": str(random.random()),
                "request": {
                    "query": chat_input,
                    "user_id": user_id
                },
                "session_id": "",
                "service_id": service_id,
                "version": "2.0"
            }
    # 将封装好的数据作为请求内容, 发送给Unit聊天机器人接口, 并得到返回结果
    res = requests.post(url=unit_chatbot_url, json=post_data)
 
 
    # 获取聊天接口返回数据
    unit_chat_obj = json.loads(res.content)
    # print(unit_chat_obj)
    # 打印返回的结果
    # 判断聊天接口返回数据是否出错 error_code == 0 则表示请求正确
    if unit_chat_obj["error_code"] != 0: return chat_reply
    # 解析聊天接口返回数据，找到返回文本内容 result -> response_list -> schema -> intent_confidence(>0) -> action_list -> say
    unit_chat_obj_result = unit_chat_obj["result"]
    unit_chat_response_list = unit_chat_obj_result["response_list"]
    # 随机选取一个"意图置信度"[+response_list[].schema.intent_confidence]不为0的技能作为回答
    unit_chat_response_obj = random.choice(
       [unit_chat_response for unit_chat_response in unit_chat_response_list if
        unit_chat_response["schema"]["intent_confidence"] > 0.0])
    unit_chat_response_action_list = unit_chat_response_obj["action_list"]
    unit_chat_response_action_obj = random.choice(unit_chat_response_action_list)
    unit_chat_response_say = unit_chat_response_action_obj["say"]
    return unit_chat_response_say

def chat(request):
    # 用户检查
    # token_string = request.COOKIES.get("token")
    # username = get_username_from_token(token_string)
    # if not username:
    #     return gen_response(401, SIGN_IN_ERROR_INFO)
    print('chat')
    # if request.method == 'POST':
    json_result = json.loads(request.body)
    print(json_result)
    text = json_result.get('text')
    botindex = json_result.get('botindex')
    print("text:",text)
    chat_reply = unit_chat(text,client_ids[botindex],client_secrets[botindex],service_ids[botindex])
    reply = HttpResponse(json.dumps({
        'code': 200,
        'text': chat_reply
    }))
    return reply
