// import '@/mock/index'
import axios from 'axios';
import API from '@/utils/API';

export default function sendMessage(_text) {
  return axios.post(API.COMUNICATE.path, {
    text: _text
  });
}
