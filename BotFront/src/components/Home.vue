<template>
  <div id="home">
    <div class="container">
      <div class="cheader">
        <header align="center">
          SECBot-{{botname}}
        </header>
        <hr />
      </div>
      <div class="content">
        <ChatList v-bind:chatList="chatlist" />
      </div>
      <div class="input-area">
        <textarea name="text" id="textarea"></textarea>
        <div class="button-area">
          <button id="send" v-on:click="send">发 送</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Avatar from 'vue-avatar';
import ChatList from '@/components/ChatList';
import sendMessage from '@/utils/communications';

export default {
  name: 'Home',
  data() {
    return {
      username: '李浩',
      botname: '小诗',
      chatlist: [
        {
          pk: 0,
          username: 'server',
          text: '昨天 12:35',
          pos: 2
        },
        {
          pk: 1,
          username: 'server',
          text: '你已添加了小诗，现在可以开始聊天了。',
          pos: 2
        },
        {
          pk: 2,
          username: '李浩',
          text: '你好',
          pos: 0
        },
        {
          pk: 3,
          username: '小诗',
          text: '你好啊',
          pos: 1
        }
      ],
      msg: 'Welcome to Your Vue.js App'
    };
  },
  components: {
    Avatar,
    ChatList
  },
  methods: {
    send: function send() {
      let text = document.querySelector('#textarea').value;
      if (!text) {
        alert('请输入内容');
        return;
      }

      // 发送消息
      let json = {};
      json.text = text;
      json.username = '李浩';
      json.pos = 0;
      json.pk = this.chatlist.length;
      this.chatlist.push(json);

      // 消息传递给后端
      sendMessage(text).then(
        (Response) => {
          if (Response.status === 200 && Response.data.code === 200) {
            console.log('Get Response', Response.data.text);
            let rjson = {};
            rjson.text = Response.data.text;
            rjson.username = '小诗';
            rjson.pos = 1;
            rjson.pk = this.chatlist.length;
            this.chatlist.push(rjson);
            console.log('chatlist:', this.chatlist);
          } else {
            console.log('Error Response');
          }
        },
        (error) => {
          console.log('No Response Error!', error);
        }
      );

      document.querySelector('#textarea').value = '';
      document.querySelector('#textarea').focus();
      // TODO: 滚动条还有问题
      let height = document.querySelector('.content').scrollHeight;
      document.querySelector('.content').scrollTop = height * 10;
      console.log(height);
    }
  },
  created() {
    // 快捷键绑定:ctrl + Enter发送消息
    const that = this;
    document.onkeyup = function Sckey(e) {
      const e1 = window.event || e;
      if (event.ctrlKey && e1.keyCode === 13) {
        that.send();
      }
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
* {
  padding: 0;
  margin: 0;
}
.container {
  margin: 0 auto;
  height: 700px;
  width: 900px;
  border-radius: 4px;
  border: 0.5px solid #e0e0e0;
  background-color: #f5f5f5;
  display: flex;
  flex-flow: column;
  overflow: hidden;
}
.cheader {
  width: calc(100% - 40px);
  height: auto;
  padding: 20px 5px 10px;
}
.content {
  width: calc(100% - 40px);
  padding: 0px 20px 20px 20px;
  overflow-y: scroll;
  flex: 1;
}
.content:hover::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0.1);
}
.bubble {
  max-width: 400px;
  padding: 10px;
  border-radius: 5px;
  position: relative;
  color: #000;
  word-wrap: break-word;
  word-break: normal;
}
.item-left .bubble {
  margin-left: 15px;
  background-color: #fff;
}
.item-left .bubble:before {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  border-left: 10px solid transparent;
  border-top: 10px solid transparent;
  border-right: 10px solid #fff;
  border-bottom: 10px solid transparent;
  left: -20px;
}
.item-right .bubble {
  margin-right: 15px;
  background-color: #9eea6a;
}
.item-right .bubble:before {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  border-left: 10px solid #9eea6a;
  border-top: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid transparent;
  right: -20px;
}
.item {
  margin-top: 15px;
  display: flex;
  width: 100%;
}
.item.item-right {
  justify-content: flex-end;
}
.item.item-center {
  justify-content: center;
}
.item.item-center span {
  font-size: 12px;
  padding: 2px 4px;
  color: #fff;
  background-color: #dadada;
  border-radius: 3px;
  -moz-user-select: none; /*火狐*/
  -webkit-user-select: none; /*webkit浏览器*/
  -ms-user-select: none; /*IE10*/
  -khtml-user-select: none; /*早期浏览器*/
  user-select: none;
}

.avatar img {
  width: 42px;
  height: 42px;
  border-radius: 50%;
}
.input-area {
  border-top: 0.5px solid #e0e0e0;
  height: 150px;
  display: flex;
  flex-flow: column;
  background-color: #fff;
}
textarea {
  flex: 1;
  padding: 5px;
  font-size: 14px;
  border: none;
  cursor: pointer;
  overflow-y: auto;
  overflow-x: hidden;
  outline: none;
  resize: none;
}
.button-area {
  display: flex;
  height: 40px;
  margin-right: 10px;
  line-height: 40px;
  padding: 5px;
  justify-content: flex-end;
}
.button-area button {
  width: 80px;
  border: none;
  outline: none;
  border-radius: 4px;
  float: right;
  cursor: pointer;
}

/* 设置滚动条的样式 */
::-webkit-scrollbar {
  width: 10px;
}
/* 滚动槽 */
::-webkit-scrollbar-track {
  box-shadow: inset006pxrgba(0, 0, 0, 0.3);
  border-radius: 8px;
}
/* 滚动条滑块 */
::-webkit-scrollbar-thumb {
  border-radius: 10px;
  background: rgba(0, 0, 0, 0);
  box-shadow: inset006pxrgba(0, 0, 0, 0.5);
}
#home{
  background:url("../assets/background.jpeg");
  background-size:100% 100%;
  width:100%;
  height:100%;
  position:fixed;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
