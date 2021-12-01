<template>
  <div id="chatList">
    <template v-for="chatBox in chatList" >
      <ChatBox :key="chatBox.pk"
                      v-bind:username = "chatBox.username"
                      v-bind:text = "chatBox.text"
                      v-bind:pos = "chatBox.pos"/>
    </template>
  </div>
</template>

<script>
import ChatBox from '@/components/ChatBox';

export default {
  name: 'ChatList',
  components: {
    ChatBox
  },
  props: {
    chatList: {
      type: Array,
      default: () => [{
        pk: 0,
        username: '李浩',
        text: '你好',
        pos: 0
      }, {
        pk: 1,
        username: '马冀',
        text: '你好啊',
        pos: 1
      }]
    }
  }
};
</script>
