<template>
  <div id="home">
    <el-container>
      <el-header>
        <el-menu class="el-menu-demo" mode="horizontal"
          background-color="#000000"
          text-color="#fff"
          active-text-color="#ffd04b">
        <el-menu-item v-if= "!ustate.online" index="1" v-on:click = "DialogVisible = 1" class="signuppage">注册</el-menu-item>
        <el-menu-item v-if= "!ustate.online" index="2" v-on:click = "DialogVisible = 2" class="loginpage">登录</el-menu-item>
        <el-menu-item v-if= "ustate.online" index="3" v-on:click = "DialogVisible = 3" class="changePw">修改密码</el-menu-item>
        <el-menu-item v-if= "ustate.online" index="4" v-on:click= "DialogVisible = 4" class="logout">退出登录</el-menu-item>
        <el-menu-item index="5" >{{ustate.username}}</el-menu-item>
      </el-menu>
      </el-header>
      <el-main>
        <img src="../assets/logo.png">
      </el-main>
      <el-footer v-if="loadingVisible">
      </el-footer>
    </el-container>
  </div>
</template>

<script>
// import {postUser, registerUser, changePW, logOut} from '@/utils/communication'

export default {
  name: 'Home',
  components: {
    Querybar,
    Signup,
    Login,
    ChangePw,
    ConfirmLogout
  },
  data () {
    return {
      query: '',
      DialogVisible: 0,
      loadingVisible: false,
      userConnectVisible: false,
      dialogVisible_logout: false,
    }
  },
  methods: {
  }
}
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
background-size:100% 100%;}
</style>
