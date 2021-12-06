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
        text: '您好,我是机器人小黄鸡,我是基于小黄鸡语料库的聊天机器人,但我不如小闲聪明,如果说错话请您不要生我的气~'
    }
]

export var hstore = {
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
      if (newValue > 0 && newValue < 6) {
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