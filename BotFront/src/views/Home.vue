<template>
  <div id="home">
    <Signup v-bind:dialogVisible= "DialogVisible == 1" v-bind:loadingVisible= "userConnectVisible" v-on:cancel= "DialogVisible = 0" v-on:confirm="toLogin" ref="sighup_dialog"/>
    <Login v-bind:dialogVisible= "DialogVisible == 2" v-bind:loadingVisible= "userConnectVisible" v-on:signup= "DialogVisible = 1" v-on:cancel="DialogVisible = 0"  v-on:confirm="login" ref="login_dialog"/>
    <ChangePw v-bind:dialogVisible = "DialogVisible == 3" v-bind:loadingVisible = "userConnectVisible" v-on:cancel= "DialogVisible = 0" v-on:confirm="changepassword" ref="changepw_dialog"/>
    <ConfirmLogout v-bind:dialogVisible = "DialogVisible == 4" v-on:cancel= "DialogVisible = 0" v-on:confirm="logout" ref="confirmLogout_dialog"/>
      <el-container>
        <el-header>
          <el-menu class="el-menu-demo" mode="horizontal" text-color="#000"  active-text-color="#6495ED" background-color="#ffffff">
            <el-menu-item v-if= "!ustate.online" index="1" v-on:click = "DialogVisible = 1" class="signuppage">注册</el-menu-item>
            <el-menu-item v-if= "!ustate.online" index="2" v-on:click = "DialogVisible = 2" class="loginpage">登录</el-menu-item>
            <el-menu-item v-if= "!ustate.online" index="3" v-on:click = "DialogVisible = 3" class="changePw">修改密码</el-menu-item>
            <el-menu-item v-if= "!ustate.online" index="4" v-on:click= "DialogVisible = 4" class="logout">退出登录</el-menu-item>
            <el-menu-item index="5" >用户名</el-menu-item>
          </el-menu>
        </el-header>
        <el-main>
          <img src="../assets/logo.png">
        </el-main>
        <el-footer v-if="loadingVisible">
          加载中...
        </el-footer>
      </el-container>
    </div>
</template>

<script>
// import {postUser, registerUser, changePW, logOut} from '@/utils/communication'
import Signup from '@/components/Signup';
import Login from '@/components/Login';
import ConfirmLogout from '@/components/ConfirmLogout';
import ChangePw from '@/components/ChangePassword';

export default {
  name: 'Home',
  components: {
    Signup,
    Login,
    ChangePw,
    ConfirmLogout
  },
  data() {
    return {
      query: '',
      DialogVisible: 1,
      loadingVisible: false,
      userConnectVisible: false,
      dialogVisible_logout: false,
      ustate: {
        online: false
      }
    };
  },
  methods: {

  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block_;
  margin: 0 10px;
}
a {
  color: #b47d34;
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
.el-header{
  font-size: 200px Extra large;
  color: rgb(248, 242, 242);
  text-align: center;
  line-height: 600px;
}
#home{
  background:url("../assets/background.jpeg");
  width:100%;
  height:100%;
  position:fixed;
  background-size:100% 100%;
}
</style>
