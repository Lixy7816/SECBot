<template>
  <el-dialog
  style="text-align: center"
  title="提示"
  :visible.sync="dialogVisible"
  :modal="false"
  :show-close=false
  :close-on-click-modal="false"
  width="30%">
    <p align = left style="font-size:130%;">您确定要退出登录吗?</p>
    <span slot="footer" class="dialog-footer">
        <el-button class="confirm" v-on:click="confirm">确 定</el-button>
        <el-button class="cancel" v-on:click="cancel">取 消</el-button>
    </span>
  </el-dialog>
</template>

<script>
export default {
  name: 'ConfirmLogout',
  props: {
    dialogVisible: {
      type: Boolean,
      default: () => true
    }
  },
  methods: {
    cancel: function cancel() {
      this.$emit('cancel');
    },
    confirm: function confirm() {
      this.$emit('confirm');
    }
  }
};
</script>
