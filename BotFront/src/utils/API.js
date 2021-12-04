const API = {
  COMUNICATE: {
    path: '/chat/',
    method: 'post'
  },
  REGISTER_USER: {
    path: '/usermanager/sign_up',
    method: 'post'
  },
  POST_USER: {
    path: '/usermanager/sign_in',
    method: 'post'
  },
  LOG_OUT: {
    path: '/usermanager/sign_out',
    method: 'get'
  },
  CHANGE_PW: {
    path: '/usermanager/modify_password',
    method: 'post'
  }
};

export default API;
