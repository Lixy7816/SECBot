<template>
  <div id="chatBox">
    <div v-if="pos===1">
      <div class="item item-left">
        <avatar
          :username="username"
          background-color="#00CED1"
          color="rgb(255, 208, 75)"
        ></avatar>
        <div class="bubble bubble-left">
          {{ text }}
        </div>
      </div>
    </div>
    <div v-else-if="pos===0">
      <div class="item item-right">
        <div class="bubble bubble-right">
          {{ text }}
        </div>
        <avatar
          :username="username"
          background-color="#fff"
          color="rgb(255, 208, 75)"
        ></avatar>
      </div>
    </div>
    <div v-else>
      <div class="item item-center">
        <span>{{ text }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import Avatar from 'vue-avatar';

export default {
  name: 'ChatBox',
  components: {
    Avatar
  },
  props: {
    username: {
      type: String,
      default: () => 'username'
    },
    text: {
      type: String,
      default: () => 'hello world'
    },
    // pos代表消息的位置,pos == 0,表示为右边(用户的消息),pos == 1,表示为左边(服务器的消息),pos == 其他,表示为中间(提示消息);
    pos: {
      type: Number,
      default: () => 2
    }
  },
  data() {
    return {};
  }
};
</script>

<style scoped>
div {
  text-align: left;
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

/* 微信色调： 9eea6a*/
.item-right .bubble {
  margin-right: 15px;
  background-color: #87CEEB;
}
.item-right .bubble:before {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  border-left: 10px solid #87CEEB;
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
</style>
