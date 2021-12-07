"""doctring"""
import json

from django.test import TestCase
from .views import chat, unit_chat
from django.test.client import RequestFactory
from django.test import Client
import requests
from usermanager.views import sign_in, sign_up

client_ids = ["Z3azDuZsqFG888EubjoR1yOR", "Z3azDuZsqFG888EubjoR1yOR",
              "Z3azDuZsqFG888EubjoR1yOR", "Z3azDuZsqFG888EubjoR1yOR"]
client_secrets = ["lFqdE8jVm6DgCCwjeTEFfehrt0g1322q", "lFqdE8jVm6DgCCwjeTEFfehrt0g1322q",
                  "lFqdE8jVm6DgCCwjeTEFfehrt0g1322q", "lFqdE8jVm6DgCCwjeTEFfehrt0g1322q"]
service_ids = ["S62219", "S62529", "S62531", "S62530"]

TEST_SIGN_UP_URL = "/usermanager/sign_up"
TEST_SIGN_IN_URL = "/usermanager/sign_in"
TEST_SIGN_OUT_URL = "/usermanager/sign_out"
TEST_CHAT_URL = "/chat/"


class MyTest(TestCase):
    def setUp(self):
        print("kaishi")

    def tearDown(self):
        print("jieshu")

    def testDemo1(self):
        result = unit_chat("早上好", client_ids[0], client_secrets[0], service_ids[0])
        print(result)

    def testDemo2(self):
        rf = RequestFactory()
        c = Client()
        # get_request = rf.get('/chat')

        post_request = rf.post('localhost:8080/chat', {'text': "中午好", 'botindex': 3}, content_type='application/json')

        response = chat(post_request)
        result = json.loads(response.content)
        print(response)
        result_code = result['code']
        assert result_code == 401


# Create your tests here.
class TestChat(TestCase):
    def test_chat(self):
        data = {
            'username': 'unittest',
            'password': '123456'
        }
        body = {
            'username': 'unittest',
            'password': '123456',
            'text': "中午好",
            'botindex': 3
        }
        c= Client()
        c.post(TEST_SIGN_UP_URL, data, content_type='application/json')
        c.post(TEST_SIGN_IN_URL, data, content_type='application/json')
        response = c.post(TEST_CHAT_URL, body, content_type='application/json')
        #print(response)
        result = json.loads(response.content)
        code = result['code']
        assert code == 200
