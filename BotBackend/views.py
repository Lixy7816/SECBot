"""doctring"""
# Create your views here.
import sys
import json
import random

#from django.shortcuts import HttpResponse
from pytz import UTC



from datetime import datetime, timedelta
#from hashlib import md5
#from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.datetime_safe import date
#from django.views.decorators.csrf import csrf_exempt
#from pytz import UTC
from usermanager.models import History
from usermanager.views import get_username_from_token, get_user_info_from_token, gen_response
from DLmodel.DLBot import botReply
import requests

sys.path.append("..")

RESULTS_PER_PAGE = getattr(settings, 'HAYSTACK_SEARCH_RESULTS_PER_PAGE', 20)

SIGN_IN_ERROR_INFO = "用户未登录或登录超时"
NOT_ADMINISTRATOR_ERROR_INFO = "用户不是管理员"
REFUSE_TO_ANSWER = "对不起,AnonymousQuery没有找到合适的答案"
DATA_ERROR_INFO = "The data does not conform to the specification"
TYPE_ERROR_INFO = "Please use POST"


class DateEncoder(json.JSONEncoder):
    '''dateencoder'''

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        return json.JSONEncoder.default(self, obj)


# 根据用户需求选择不同的AI进行回复
# AI依次是:闲聊,诗词,问答,影视
client_ids = ["Z3azDuZsqFG888EubjoR1yOR", "Z3azDuZsqFG888EubjoR1yOR",
              "Z3azDuZsqFG888EubjoR1yOR", "Z3azDuZsqFG888EubjoR1yOR"]
client_secrets = ["lFqdE8jVm6DgCCwjeTEFfehrt0g1322q", "lFqdE8jVm6DgCCwjeTEFfehrt0g1322q",
                  "lFqdE8jVm6DgCCwjeTEFfehrt0g1322q", "lFqdE8jVm6DgCCwjeTEFfehrt0g1322q"]
service_ids = ["S62219", "S62529", "S62531", "S62530"]


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
    chat_reply = "不好意思，我们正在学习，稍后再回复您。"
    # 根据 client_id 与 client_secret 获取access_token
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client" \
          "_credentials&client_id=%s&client_secret=%s" % (client_id, client_secret)
    res = requests.get(url)
    access_token = eval(res.text)["access_token"]
    # 根据 access_token 获取聊天机器人接口数据
    unit_chatbot_url = "https://aip.baidubce.com/rpc/2.0/unit/service/" \
                       "chat?access_token=" + access_token
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
    if unit_chat_obj["error_code"] != 0:
        return chat_reply
    # 解析聊天接口返回数据，找到返回文本内容 result -> response_list -> schema
    # -> intent_confidence(>0) -> action_list -> say
    unit_chat_obj_result = unit_chat_obj["result"]
    unit_chat_response_list = unit_chat_obj_result["response_list"]
    # 随机选取一个"意图置信度"[+response_list[].schema.intent_confidence]不为0的技能作为回答
    goodans = [unit_chat_response for unit_chat_response in unit_chat_response_list if unit_chat_response["schema"]
               ["intent_confidence"] > 0.0]
    if goodans == []:
        return chat_reply
    unit_chat_response_obj = random.choice(goodans)
    unit_chat_response_action_list = unit_chat_response_obj["action_list"]
    unit_chat_response_action_obj = random.choice(
        unit_chat_response_action_list)
    unit_chat_response_say = unit_chat_response_action_obj["say"]


    return unit_chat_response_say


def chat(request):
    # 用户检查
    token_string = request.COOKIES.get("token")
    username = get_username_from_token(token_string)
    if not username:
        return gen_response(401, SIGN_IN_ERROR_INFO)
    print('chat')
    # if request.method == 'POST':
    json_result = json.loads(request.body)
    print(json_result)
    text = json_result.get('text')

    botindex = json_result.get('botindex')
    if botindex < 4:
        chat_reply = unit_chat(
            text, client_ids[botindex], client_secrets[botindex], service_ids[botindex])
    else:
        chat_reply = botReply(text)

    # 如果接受到的内容为空，则给出相应的回复
    if chat_reply == ' ' or chat_reply == '':
        chat_reply = '不好意思，我们正在学习，稍后再回复您。'

    try:
        history = History(username=username, bot_id=botindex,
                          query=text, answer=chat_reply)
        history.full_clean()
        history.save()
    except BaseException as _e:
        return gen_response(200, {
            'code': 200,
            'text': chat_reply
        }, username)

    return gen_response(200, {
            'code': 200,
            'text': chat_reply
        }, username)
    # reply = HttpResponse(json.dumps({
    #     'code': 200,
    #     'text': chat_reply
    # }))
    # return reply
