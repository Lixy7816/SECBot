<template>
  <el-dialog
  style="text-align: center"
  title="修改密码"
  :visible.sync="dialogVisible"
  :modal="false"
  :show-close=false
  :close-on-click-modal="false"
  width="80%">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" class="ruleForm">
        <el-form-item label="原密码" prop="old_password">
          <el-input v-model="ruleForm.old_password" placeholder="old_password" show-password></el-input>
          <!-- <span v-if="state.username_valid===false" style="color: red">请设置合法用户名!</span> -->
        </el-form-item>
        <el-form-item label="新密码" prop="password">
            <el-input v-model="ruleForm.password" placeholder="password" show-password></el-input>
        </el-form-item>
        <el-form-item label="确认密码" prop="password2">
            <el-input v-model="ruleForm.password2" placeholder="confirm password" show-password></el-input>
            <span v-if="ruleForm.pwValid===false" style="color: red">请保证密码一致!</span>
        </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
        <el-button class="confirm" v-on:click="confirm('ruleForm')">确 定</el-button>
        <el-button class="cancel" v-on:click="cancel">取 消</el-button>
    </span>
  </el-dialog>
</template>

<script>
export default {
  name: 'ChangePw',
  props: {
    dialogVisible: {
      type: Boolean,
      default: () => true
    }
  },
  data() {
    let validatePass2 = (rule, value, callback) => {
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
        old_password: '',
        password: '',
        password2: ''
      },
      rules: {
        old_password: [
          { required: true, message: '请输入原密码', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入新密码', trigger: 'blur' }
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
    confirm: function cancel(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$emit('confirm', this.ruleForm.old_password, this.ruleForm.password);
          return true;
        }
        return false;
      });
    }
  }
};
</script>
