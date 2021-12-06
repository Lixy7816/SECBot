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
    botindex: 0,
    online: false
  },
  set_user(newValue) {
    this.state.username = newValue;
    return;
  },
  set_bot(newValue) {
    if (newValue > 0 && newValue < 5) {
      let index = newValue - 1;
      this.state.botindex = index;
      this.state.botname = botnames[index];
      return;
    } else {
      console.log('Error!The index is not in range');
      return;
    }
  },
  set_online(newValue) {
    this.state.online = newValue;
    return;
  }
};
