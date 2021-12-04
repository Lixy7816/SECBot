<template>
  <el-dialog
  style="text-align: center"
  title="新用户注册"
  :visible.sync="dialogVisible"
  :modal="false"
  :show-close=false
  :close-on-click-modal="false"
  width="80%">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="ruleForm.username" placeholder="username"></el-input>
          <!-- <span v-if="state.username_valid===false" style="color: red">请设置合法用户名!</span> -->
        </el-form-item>
        <el-form-item label="密码" prop="password">
            <el-input v-model="ruleForm.password" placeholder="passowrd" show-password></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="password2">
            <el-input v-model="ruleForm.password2" placeholder="confirm password" show-password></el-input>
        </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
        <el-button class="confirm" v-on:click="confirm('ruleForm')">确 定</el-button>
        <el-button class="cancel" v-on:click="cancel">取 消</el-button>
    </span>
    <div v-if="loadingVisible" class="loadingio-spinner-spin-5xzwelrv9ro"><div class="ldio-itdzyrvokrd"><div><div></div></div><div><div></div></div><div><div></div></div><div><div></div></div><div><div></div></div><div><div></div></div><div><div></div></div><div><div></div></div></div></div>
  </el-dialog>
</template>

<script>

export default {
  name: 'Signup',
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
    let validatePass2 = (value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.ruleForm.password) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    return {
      ruleForm: {
        username: '',
        password: '',
        password2: ''
      },
      rules: {
        username: [
          { required: true, message: '请设置用户名', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ],
        password2: [
          { required: true, validator: validatePass2, trigger: 'blur' }
        ]
      }
    };
  },
  methods: {
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
