'''views'''
import json
import sys
from datetime import datetime, timedelta
from hashlib import md5
from django.shortcuts import HttpResponse
from django.core.exceptions import ValidationError
from django.utils.datetime_safe import date
from django.views.decorators.csrf import csrf_exempt
from pytz import UTC
from .models import User, History, Token

sys.path.append("..")

SIGN_IN_ERROR_INFO = "用户未登录或登录超时"
DATA_ERROR_INFO = "The data does not conform to the specification"
TYPE_ERROR_INFO = "Please use POST"
# Create your views here.

class DateEncoder(json.JSONEncoder):
    '''dateencoder'''

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        return json.JSONEncoder.default(self, obj)


def gen_token(username):
    '''generate token for the user'''
    Token.objects.filter(expires_at__lt=datetime.now()).delete()
    Token.objects.filter(username=username).delete()
    user = User.objects.filter(username=username).first()
    if not user:
        return gen_response(400, "User not found")
    expires_at = datetime.now() + timedelta(minutes=20)
    hl = md5()
    hl.update((expires_at.strftime('%Y-%m-%d %H:%M:%S') + str(user.id)).encode(encoding='utf-8'))
    token_string = hl.hexdigest()
    token = Token(username=username, token=token_string,
                  expires_at=expires_at, is_manager=user.is_manager)
    try:
        token.full_clean()
        token.save()
    except ValidationError as _:
        return ""
    return token_string


def renew_token(token_string):
    '''renew_token'''
    Token.objects.filter(token=token_string)

def gen_user_info(username):
    '''generate response'''
    user = User.objects.filter(username=username).first()
    return {'id': user.id,
            'username': user.username,
            'password': user.password,
            'is_manager': user.is_manager}


def gen_response(code, data, username=None):
    '''generate response'''
    res = HttpResponse(json.dumps({
        'code': code,
        'data': data
    }, cls=DateEncoder), content_type="application/json", status=code)

    if username:
        token_string = gen_token(username)
        res.set_cookie("token", token_string)
    return res


def get_user_info_from_token(token_string):
    '''get_user_info_from_token'''
    token = Token.objects.filter(token=token_string).first()
    if not token:
        return "", False
    expire_time = token.expires_at
    if expire_time < UTC.localize(datetime.now()):
        return "", False
    return token.username, token.is_manager


def get_username_from_token(token_string):
    '''get_username_from_token'''
    username, _ = get_user_info_from_token(token_string)
    return username

@csrf_exempt
def sign_up(request):
    '''sign_up'''
    if request.method == 'POST':
        try:
            json_result = json.loads(request.body)
            print('sign up',json_result)
            username = json_result.get('username')
            password = json_result.get('password')
        except:
            return gen_response(400, DATA_ERROR_INFO)
    else:
        return gen_response(400, TYPE_ERROR_INFO)
    user = User.objects.filter(username=username).first()
    if not user:
        is_manager = False
        if username == "Anonymous":
            is_manager = True
        user = User(username=username, password=password, is_manager=is_manager)
        try:
            # 注意在调用full_clean()时Django会自动检测字段的有效性，这个有效性检测包括检测CharField是否满足最大长度限制
            user.full_clean()
            # 存入数据库
            user.save()
        except ValidationError as e:
            return gen_response(400, "Validation Error of user: {}".format(e))
        return gen_response(200, {"is_manager": user.is_manager})

    return gen_response(400, "该用户名已被注册")


@csrf_exempt
def sign_in(request):
    '''sign_in'''
    if request.method == 'POST':
        try:
            json_result = json.loads(request.body)
            print('sign in',json_result)
            username = json_result.get('username')
            password = json_result.get('password')
        except:
            return gen_response(400, DATA_ERROR_INFO)
    else:
        return gen_response(400, TYPE_ERROR_INFO)
    user = User.objects.filter(username=username, password=password).first()
    if not user:
        return gen_response(400, "用户名或密码错误")
    return gen_response(200, {"is_manager": user.is_manager}, user.username)


@csrf_exempt
def sign_out(request):
    '''sign_out'''
    token_string = request.COOKIES.get("token")
    Token.objects.filter(token=token_string).delete()
    return gen_response(200, '')


@csrf_exempt
def modify_password(request):
    '''modify_password'''
    token_string = request.COOKIES.get("token")
    username = get_username_from_token(token_string)
    if not username:
        return gen_response(401, SIGN_IN_ERROR_INFO)
    if request.method == 'POST':
        try:
            json_result = json.loads(request.body)
            password = json_result.get('password')
            new_password = json_result.get('new_password')
        except:
            return gen_response(400, DATA_ERROR_INFO)
    else:
        return gen_response(400, TYPE_ERROR_INFO)
    user = User.objects.filter(username=username, password=password).first()
    if not user:
        return gen_response(400, "密码错误,请检查您的输入")
    User.objects.filter(username=username, password=password).update(password=new_password)
    return gen_response(200, {}, user.username)
