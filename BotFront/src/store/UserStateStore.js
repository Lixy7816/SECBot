export const botnames = [
  'SECBot-小闲',
  'SECBot-小诗',
  'SECBot-小问',
  'SECBot-小影'
];

export var ustore = {
  state: {
    username: 'Lixy',
    botname: '小闲',
    botindex: 1,
    online: false
  },
  set_user(newValue) {
    this.state.username = newValue;
  },
  set_bot(newValue) {
    this.state.botindex = newValue - 1;
    this.state.botname = botnames[newValue - 1];
  },
  set_online(newValue) {
    this.state.online = newValue;
  }
};
