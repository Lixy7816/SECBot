// import '@/mock/index'
import axios from 'axios';
import API from '@/utils/API';

// 发送信息
export function sendMessage(_text) {
  return axios.post(API.COMUNICATE.path, {
    text: _text
  });
}

// 添加用户
export function registerUser (_username, _password) {
  return axios.post(API.REGISTER_USER.path, {
    username: _username,
    password: _password
  });
}

// 用户登录
export function postUser (_username, _password) {
  return axios.post(API.POST_USER.path, {
    username: _username,
    password: _password
  });
}

// 退出登录
export function logOut () {
  return axios.get(API.LOG_OUT.path);
}

//  更改密码
export function changePW (_username, _password, _new_password) {
  return axios.post(API.CHANGE_PW.path, {
    username: _username,
    password: _password,
    new_password: _new_password
  });
}