'''model'''
from django.db import models

# Create your models here.

#用户信息表
class User(models.Model):
    '''user'''
    # 用户名
    username = models.CharField('username', max_length=20)
    # 密码
    password = models.CharField('password', max_length=20)
    # 是否为管理员
    is_manager = models.BooleanField('manager', default=False)

    class Meta:
        db_table = 'Users'

#历史记录表
class History(models.Model):
    '''history'''
    # 哪个用户的记录
    username = models.CharField('username', max_length=20)
    # 答案对应文章的id
    doc_id = models.IntegerField('doc_id')
    # 查询的问题
    query = models.CharField('query', max_length=64)
    # 问题的最佳答案
    answer = models.CharField('answer', max_length=64)
    # 时间戳
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'History'

class Token(models.Model):
    '''token'''
    # The user
    username = models.CharField('username', max_length=20)
    # Is manager
    is_manager = models.BooleanField("is manager", default=False)
    # The token
    token = models.CharField('token', max_length=32)
    # The token expires at this time
    expires_at = models.DateTimeField()

    class Meta:
        db_table = 'Token'