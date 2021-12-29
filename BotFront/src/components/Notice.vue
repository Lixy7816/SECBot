<template>
  <el-dialog
  :visible.sync="dialogVisible"
  :modal="false"
  :show-close=false
  :close-on-click-modal="false"
  width="70%">
  <font size="5">功能说明</font>
  <el-divider></el-divider>
  <p align="left">
    {{text0}}<br>
    {{text1}}<br>
    {{text2}}<br>
    {{text3}}<br>
    {{text4}}<br>
    {{text5}}<br>
  </p>
    <span slot="footer" class="dialog-footer">
        <el-button class="cancel" v-on:click="cancel">确定</el-button>
    </span>
  </el-dialog>
</template>

<script>
export default {
  name: 'Notice',
  props: {
    dialogVisible: {
      type: Boolean,
      default: () => true
    }
  },
  data() {
    return {
      text0: '欢迎来到SECBot智能聊天区,我们提供了以下机器人陪您畅聊:',
      text1: '1.闲聊机器人:可以和您进行一般的聊天和问候;',
      text2: '2.诗词机器人:您给出一个主题,bot会依据您给出的主题作诗;',
      text3: '3.问答机器人:您可以提出问题,如“什么是xx？”,bot会给出相应的答案,目前支持成语和一些通用知识的问答;',
      text4: '4.影视机器人:可以陪您进行影视相关的聊天,包括电影内容,演员,故事情节等多方面内容;',
      text5: '5.小黄鸡机器人:同样提供闲聊功能,但是能力比较弱~'
    };
  },
  methods: {
    cancel: function cancel() {
      this.$emit('cancel');
    }
  }
};
</script>
