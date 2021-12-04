export var ustore = {
  state: {
    username: '请登录',
    botname: '小闲',
    online: false
  },
  botnames: [
    "SECBot-小闲",
    "SECBot-小诗",
    "SECBot-小问",
    "SECBot-小影"
  ],
  set_user (newValue) {
    this.state.username = newValue;
  },
  set_bot (newValue) {
    this.state.botname = botnames[newValue-1];
  },
  set_online (newValue) {
    this.state.online = newValue;
  }
}
