<template>
  <el-dialog
        style="text-align: center"
        title="登录"
        :visible.sync="dialogVisible"
        :close-on-click-modal="false"
        :show-close=false
        :modal="false"
        width="80%">

    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px">
        <el-form-item label="用户名" prop="username">
            <el-input v-model="ruleForm.username" placeholder="username"></el-input>
            <!-- <span v-if="state.username_valid===false" style="color: red">请设置合法用户名!</span> -->
        </el-form-item>
        <el-form-item label="密码" prop="password">
            <el-input v-model="ruleForm.password" placeholder="password"  show-password></el-input>
        </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
                <el-button class="signup" v-on:click="signup">新用户注册</el-button>
                <el-button class="confirm" v-on:click="confirm('ruleForm')">确 定</el-button>
                <el-button class="cancel" v-on:click="cancel">取 消</el-button>
    </span>
    <div v-if="loadingVisible" class="loadingio-spinner-spin-5xzwelrv9ro"><div class="ldio-itdzyrvokrd"><div><div></div></div><div><div></div></div><div><div></div></div><div><div></div></div><div><div></div></div><div><div></div></div><div><div></div></div><div><div></div></div></div></div>
  </el-dialog>
</template>

<script>
export default {
  name: 'Login',
  props: {
    dialogVisible: {
      type: Boolean,
      default: () => true
    },
    loadingVisible: {
      type: Boolean,
      default: () => false
    }
  },
  data() {
    return {
      ruleForm: {
        username: '',
        password: ''
      },
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ]
      }
    };
  },
  methods: {
    signup: function signup() {
      this.$emit('signup');
    },
    cancel: function cancel() {
      this.$emit('cancel');
    },
    confirm: function confirm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$emit('confirm', this.ruleForm.username, this.ruleForm.password);
          return true;
        }
        return false;
      });
    }
  }
};
</script>

<style scoped>
@import '../assets/connect.css';
</style>
