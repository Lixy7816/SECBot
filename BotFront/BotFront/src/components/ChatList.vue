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
      default: () => []
    }
  }
};
</script>
