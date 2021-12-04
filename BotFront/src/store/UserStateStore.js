export var ustore = {
  state: {
    username: '请登录',
    botname: '小闲',
    online: false
  },
  set_user (newValue) {
    this.state.username = newValue;
  },
  set_bot (newValue) {
    this.state.botname = newValue;
  },
  set_online (newValue) {
    this.state.online = newValue;
  }
}
