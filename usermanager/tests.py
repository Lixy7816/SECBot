'''unit test'''
import json
import pytest
from django.test import TestCase
from django.test.client import RequestFactory
from .views import sign_in, sign_out, sign_up, view_history, modify_password
# Create your tests here.
from django.test import Client

TEST_SIGN_UP_URL = "/usermanager/sign_up"
TEST_SIGN_IN_URL = "/usermanager/sign_in"
TEST_SIGN_OUT_URL = "/usermanager/sign_out"

@pytest.mark.django_db
class SignUpTests(TestCase):
    '''query test'''
    def test_sign_up(self):
        '''query test'''
        rf = RequestFactory()
        data = {
            'username':'unittest',
            'password':'123456'
        }
        request = rf.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        response = sign_up(request)

        result = json.loads(response.content)
        code = result['code']
        assert code == 200

class SignInTests(TestCase):
    '''query test'''
    def test_sign_in(self):
        '''query test'''
        c = Client()
        rf1 = RequestFactory()
        data = {
            'username':'unittest',
            'password':'123456'
        }
        response = c.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        response = c.post(TEST_SIGN_IN_URL, data, content_type='application/json')
        print(c.cookies.items())
        result = json.loads(response.content)
        code = result['code']
        assert code == 200

class SignOutTests(TestCase):
    '''query test'''
    def test_sign_out(self):
        '''query test'''
        rf1 = RequestFactory()
        data = {
            'username':'unittest',
            'password':'123456'
        }
        rf1.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        rf2 = RequestFactory()
        request2 = rf2.post(TEST_SIGN_IN_URL, data, content_type='application/json')
        rf3 = RequestFactory()
        request3 = rf3.post(TEST_SIGN_IN_URL)
        response = sign_out(request3)
        result = json.loads(response.content)
        code = result['code']
        assert code == 200