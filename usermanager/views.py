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
from docmanager.models import Doc
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
