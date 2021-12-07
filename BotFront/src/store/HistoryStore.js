import { ustore, botnames } from '@/store/UserStateStore';

export const defaultmessages = [
  {
    index: 1,
    text: '您好,我是机器人小闲,我可以陪您聊天唠嗑哦~'
  },
  {
    index: 2,
    text: '您好,我是机器人小诗,您输入一个主题,我就可以为您作诗~'
  },
  {
    index: 3,
    text: '您好,我是机器人小问,您有什么问题都可以问问我啦~'
  },
  {
    index: 4,
    text: '您好,我是机器人小影,我可以陪您聊电影,您喜欢什么电影呢~'
  },
  {
    index: 5,
    text:
      '您好,我是机器人小黄鸡,我是基于小黄鸡语料库的聊天机器人,但我不如小闲聪明,如果说错话请您不要生我的气~'
  }
];

// 每次储存一对对话
export var hstore = {
  state: [[], [], [], [], []],
  add_one_history(bot_index, _username, _text, _pos) {
    let pk1 = this.state[bot_index].length;
    this.state[bot_index].push({
      pk: pk1,
      username: _username,
      text: _text,
      pos: _pos
    });
  },
  add_historys(history) {
    let botindex = history.bot_id;
    let query = history.query;
    let answer = history.answer;
    let botname = botnames[botindex].slice(8);
    let username = ustore.state.username;
    this.add_one_history(botindex, username, query, 0);
    this.add_one_history(botindex, botname, answer, 1);
    return;
  },
  add_default_message() {
    for (let index = 0; index < 5; index += 1) {
      this.state[index].push({
        pk: 0,
        username: botnames[index].slice(8),
        text: defaultmessages[index].text,
        pos: 1
      });
    }
    return;
  },
  clear() {
    this.state = [[], [], [], [], []];
  }
};
