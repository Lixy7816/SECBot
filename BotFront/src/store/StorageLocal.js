export const STORAGE_KEY = 'lixy-15asf8f8wf1sdhg8j';
export var localStore = {
  save_json(item, json) {
    window.localStorage.setItem(STORAGE_KEY + item, JSON.stringify(json));
  },
  get_json(item) {
    return JSON.parse(window.localStorage.getItem(STORAGE_KEY + item) || '[]');
  },
  remove_json(item) {
    window.localStorage.removeItem(STORAGE_KEY + item);
  }
};

// 获取cookie中的token
export function get_token(cookie) {
  let c_name = 'token';
  if (cookie.length > 0) {
    let c_start = cookie.indexOf(c_name + '=');
    if (c_start !== -1) {
      c_start = c_start + c_name.length + 1;
      let c_end = cookie.indexOf(';', c_start);
      if (c_end === -1) c_end = cookie.length;
      return unescape(cookie.substring(c_start, c_end));
    }
  }
  return '';
}
