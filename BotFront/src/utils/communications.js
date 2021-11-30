// import '@/mock/index'
import axios from 'axios'
import API from '@/utils/API'

export function sendMessage (_text) {
  return axios.post(API.COMUNICATE.path, {
    text: _text
  })
}

// // 添加用户
// export function registerUser (_username, _password) {
//   return axios.post(API.REGISTER_USER.path, {
//     username: _username,
//     password: _password
//   })
// }

// // 用户登录
// export function postUser (_username, _password) {
//   return axios.post(API.POST_USER.path, {
//     username: _username,
//     password: _password
//   })
// }

// // 退出登录
// export function logOut () {
//   return axios.get(API.LOG_OUT.path)
// }

// //  更改密码
// export function changePW (_username, _password, _new_password) {
//   return axios.post(API.CHANGE_PW.path, {
//     username: _username,
//     password: _password,
//     new_password: _new_password
//   })
// }

// // 查询答案
// export function postQuery (query) {
//   return axios.get(API.POST_QUERY.path, {
//     params: {
//       q: query
//     }
//   })
// }

// // 查询历史记录
// export function getHistory (_username) {
//   return axios.post(API.VIEW_HISTORY.path, {
//     username: _username
//   })
// }

// // 添加文档
// export function addArticle (_title, _context) {
//   return axios.post(API.ADD_FILE.path, {
//     title: _title,
//     context: _context
//   })
// }

// //  删除文档
// export function deleteArticle (id) {
//   return axios.post(API.DELETE_FILE.path, {
//     id: id
//   })
// }

// //  获取含某一页的文档
// export function get_docs (_filter, _docs_per_page, _page_id) {
//   return axios.post(API.VIEW_DOCS.path, {
//     _filter: _filter,
//     docs_per_page: _docs_per_page,
//     page_id: _page_id
//   })
// }
