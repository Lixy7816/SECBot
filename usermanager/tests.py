'''unit test'''
import json
import pytest
from django.test import TestCase
from django.test.client import RequestFactory
from .views import sign_in, sign_out, sign_up, view_history, modify_password, gen_token, gen_response
# Create your tests here.
from django.test import Client

TEST_SIGN_UP_URL = "/usermanager/sign_up"
TEST_SIGN_IN_URL = "/usermanager/sign_in"
TEST_SIGN_OUT_URL = "/usermanager/sign_out"
TEST_MODIFY_PASSWORD = "/usermanager/modify_password"
TEST_VIEW_HISTORY = "/usermanager/view_history"

SIGN_IN_ERROR_INFO = "用户未登录或登录超时"
DATA_ERROR_INFO = "The data does not conform to the specification"
TYPE_ERROR_INFO = "Please use POST"


@pytest.mark.django_db
class SignUpTests(TestCase):
    '''query test'''

    def test_sign_up(self):
        '''query test'''
        rf = RequestFactory()
        data = {
            'username': 'unittest',
            'password': '123456'
        }
        request = rf.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        response = sign_up(request)

        result = json.loads(response.content)
        code = result['code']
        assert code == 200

    def test_sign_up_fork1(self):
        rf = RequestFactory()
        data = {
            'username': 'unittest',
            'password': '123456'
        }
        request = rf.get(TEST_SIGN_UP_URL, data, content_type='application/json')
        response = sign_up(request)

        result = json.loads(response.content)
        code = result['code']
        assert code == 400

    def test_sign_up_fork2(self):
        rf = RequestFactory()
        data = {
            'username': 'Anonymous',
            'password': '123456'
        }
        request = rf.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        response = sign_up(request)

        result = json.loads(response.content)
        code = result['code']
        assert code == 200

    def test_sign_up_fork3(self):
        rf = RequestFactory()
        data = {
            'username': 'unittest',
            'password': '12345690abcdefghikjlmnopq'
        }
        request = rf.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        response = sign_up(request)

        result = json.loads(response.content)
        code = result['code']
        assert code == 400

    def test_sign_up_fork4(self):
        rf = RequestFactory()
        data = {
            'username': 'unittest',
            'password': '123456'
        }
        rf1 = RequestFactory()
        request = rf.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        response = sign_up(request)
        request1 = rf1.post(TEST_SIGN_UP_URL, data, content_type='application/json')

        response1 = sign_up(request1)

        result = json.loads(response1.content)
        code = result['code']
        assert code == 400

    def test_sign_up_fork5(self):
        rf = RequestFactory()
        data = {
            "lbbljbavskjbvlakjbsvjakblbasjb"
        }
        request = rf.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        response = sign_up(request)

        result = json.loads(response.content)
        code = result['code']
        assert code == 400


class SignInTests(TestCase):
    '''query test'''

    def test_sign_in(self):
        '''query test'''
        c = Client()
        rf1 = RequestFactory()
        data = {
            'username': 'unittest',
            'password': '123456'
        }
        response = c.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        response = c.post(TEST_SIGN_IN_URL, data, content_type='application/json')
        # print(c.cookies.items())
        result = json.loads(response.content)
        code = result['code']
        assert code == 200

    def test_sign_in_fork1(self):
        c = Client()
        rf1 = RequestFactory()
        data = {
            'username': 'unittest',
            'password': '123456'
        }
        response = c.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        response = c.get(TEST_SIGN_IN_URL, data, content_type='application/json')
        # print(c.cookies.items())
        result = json.loads(response.content)
        code = result['code']
        assert code == 400

    def test_sign_in_fork2(self):
        c = Client()
        rf1 = RequestFactory()
        data = {
            "asneln;lekn;knev;n"
        }
        response = c.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        response = c.post(TEST_SIGN_IN_URL, data, content_type='application/json')
        # print(c.cookies.items())
        result = json.loads(response.content)
        code = result['code']
        assert code == 400

    def test_sign_in_fork3(self):
        c = Client()
        rf1 = RequestFactory()
        data = {
            'username': 'unittest',
            'password': '123456'
        }
        data_new = {
            'username': 'hhhhhhhhhhh',
            'password': '123456'
        }
        response = c.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        response = c.post(TEST_SIGN_IN_URL, data_new, content_type='application/json')
        # print(c.cookies.items())
        result = json.loads(response.content)
        code = result['code']
        assert code == 400


class SignOutTests(TestCase):
    '''query test'''

    def test_sign_out(self):
        '''query test'''
        rf1 = RequestFactory()
        data = {
            'username': 'unittest',
            'password': '123456'
        }
        rf1.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        rf2 = RequestFactory()
        rf2.post(TEST_SIGN_IN_URL, data, content_type='application/json')
        rf3 = RequestFactory()
        request3 = rf3.post(TEST_SIGN_IN_URL)
        response = sign_out(request3)
        result = json.loads(response.content)
        code = result['code']
        assert code == 200


class GenResponseTest(TestCase):
    def test_gen_response(self):
        res = gen_response(200, 'success', 'mj')
        # print(res)


class ModifyPasswordTests(TestCase):
    '''query test'''

    def test_modify_password(self):
        '''query test'''
        c = Client()

        data = {
            'username': 'unittest',
            'password': '123456'
        }
        data_new = {
            'username': 'unittest',
            'password': '123456',
            'new_password': '654321'
        }
        c.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        c.post(TEST_SIGN_IN_URL, data, content_type='application/json')
        response = c.post(TEST_MODIFY_PASSWORD, data_new, content_type='application/json')
        # print(c.cookies.items())
        result = json.loads(response.content)
        code = result['code']
        assert code == 200

    def test_modify_password_fork1(self):
        c = Client()

        data = {
            'username': 'unittest',
            'password': '123456'
        }
        data_new = {
            'username': 'unittest',
            'password': '123456',
            'new_password': '654321'
        }
        c.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        c.post(TEST_SIGN_IN_URL, data, content_type='application/json')
        response = c.get(TEST_MODIFY_PASSWORD, data_new, content_type='application/json')
        # print(c.cookies.items())
        result = json.loads(response.content)
        code = result['code']
        assert code == 400

    def test_modify_password_fork2(self):
        c = Client()

        data = {
            'username': 'unittest',
            'password': '123456'
        }
        data_new = {
            "bliub-1qlib": "liuweliub",
            "qliublu": "kb`lub"
        }
        c.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        c.post(TEST_SIGN_IN_URL, data, content_type='application/json')
        response = c.get(TEST_MODIFY_PASSWORD, data_new, content_type='application/json')
        # print(c.cookies.items())
        result = json.loads(response.content)
        code = result['code']
        assert code == 400

    def test_modify_password_fork3(self):
        c = Client()

        data = {
            'username': 'unittest',
            'password': '123456'
        }
        data_new = {
            'username': 'unittest',
            'password': '123456789',
            'new_password': '654321'
        }
        c.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        c.post(TEST_SIGN_IN_URL, data, content_type='application/json')
        response = c.post(TEST_MODIFY_PASSWORD, data_new, content_type='application/json')
        # print(c.cookies.items())
        result = json.loads(response.content)
        code = result['code']
        assert code == 400

class ViewHistoryTest(TestCase):
    def test_view_history(self):
        c = Client()
        data = {
            'username': 'unittest',
            'password': '123456',
            'text': "中午好",
            'botindex': 3
        }
        c.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        c.post(TEST_SIGN_IN_URL, data, content_type='application/json')
        response = c.post(TEST_VIEW_HISTORY, data, content_type='application/json')
        result = json.loads(response.content)
        code = result['code']
        assert code == 200

    def test_view_history_exception(self):
        c = Client()
        data = {
            'username': 'unittest',
            'password': '123456',
            'text': "中午好",
            'botindex': 3
        }
        new_data = {
            'username': 'hhhhh',
            'password': '123456',
            'text': "中午好",
            'botindex': 3
        }
        # c.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        # c.post(TEST_SIGN_IN_URL, data, content_type='application/json')
        response = c.post(TEST_VIEW_HISTORY, data, content_type='application/json')
        result = json.loads(response.content)
        code = result['code']
        assert code == 401
