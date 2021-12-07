<template>
  <div id="home">
    <Signup
      v-bind:dialogVisible="DialogVisible == 1"
      v-bind:loadingVisible="userConnectVisible"
      v-on:cancel="DialogVisible = 0"
      v-on:confirm="toLogin"
      ref="sighup_dialog"
    />
    <Login
      v-bind:dialogVisible="DialogVisible == 2"
      v-bind:loadingVisible="userConnectVisible"
      v-on:signup="DialogVisible = 1"
      v-on:cancel="DialogVisible = 0"
      v-on:confirm="login"
      ref="login_dialog"
    />
    <ChangePw
      v-bind:dialogVisible="DialogVisible == 3"
      v-bind:loadingVisible="userConnectVisible"
      v-on:cancel="DialogVisible = 0"
      v-on:confirm="changepassword"
      ref="changepw_dialog"
    />
    <ConfirmLogout
      v-bind:dialogVisible="DialogVisible == 4"
      v-on:cancel="DialogVisible = 0"
      v-on:confirm="logout"
      ref="confirmLogout_dialog"
    />
    <el-container>
      <el-header>
        <el-menu
          class="el-menu-demo"
          mode="horizontal"
          text-color="#000"
          active-text-color="#6495ED"
          background-color="#ffffff"
        >
          <el-menu-item
            v-if="!ustate.online"
            index="1"
            v-on:click="DialogVisible = 1"
            class="signuppage"
            >注册</el-menu-item
          >
          <el-menu-item
            v-if="!ustate.online"
            index="2"
            v-on:click="DialogVisible = 2"
            class="loginpage"
            >登录</el-menu-item
          >
          <el-menu-item
            v-if="!ustate.online"
            index="3"
            v-on:click="DialogVisible = 3"
            class="changePw"
            >修改密码</el-menu-item
          >
          <el-menu-item
            v-if="!ustate.online"
            index="4"
            v-on:click="DialogVisible = 4"
            class="logout"
            >退出登录</el-menu-item
          >
          <el-menu-item index="5">{{ustate.username}}</el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
        <ChooseBot v-on:choseABot="choseABot" />
      </el-main>
      <el-footer v-if="loadingVisible">
        加载中...
      </el-footer>
    </el-container>

    <el-drawer
      title="title"
      :visible.sync="DrawVisible"
      :with-header="false"
      :modal="false"
      size="100%"
      style="overflow:hidden;"
    >
      <ChatRoom ref="ctroom" v-on:back="DrawVisible = false"/>
    </el-drawer>
  </div>
</template>

<script>
// registerUser, changePW, logOut
import { registerUser, postUser } from '@/utils/communications';
import { ustore } from '@/store/UserStateStore';
import { defaultmessages } from '@/store/HistoryStore';
import { localStore } from '@/store/StorageLocal';
import Signup from '@/components/Signup';
import Login from '@/components/Login';
import ConfirmLogout from '@/components/ConfirmLogout';
import ChangePw from '@/components/ChangePassword';
import ChooseBot from '@/components/ChooseBot';
import ChatRoom from '@/components/ChatRoom';

let MES_INFO = 0;
let MES_ERROR = 1;
let MES_SUCC = 2;

export default {
  name: 'Home',
  components: {
    Signup,
    Login,
    ChangePw,
    ConfirmLogout,
    ChooseBot,
    ChatRoom
  },
  data() {
    return {
      query: '',
      DialogVisible: 1,
      DrawVisible: false,
      loadingVisible: false,
      userConnectVisible: false,
      dialogVisible_logout: false,
      ustate: ustore.state,
    };
  },
  methods: {
    // 1.错误处理代码
    error_handle: function error_handle(error) {
      // TODO: 补全错误处理
      console.log(error);
    },
    // 2.通用提示信息
    tips: function tips(wait_time, message_type, _message) {
      this.timer = setTimeout(() => {
        if (message_type === MES_ERROR) {
          this.$notify.error({
            position: 'top-left',
            offset: 100,
            duration: 1000,
            title: '错误提示',
            message: _message
          });
        } else if (message_type === MES_INFO) {
          this.$notify.info({
            position: 'top-left',
            title: '提示',
            offset: 100,
            duration: 1000,
            message: _message
          });
        } else if (message_type === MES_SUCC) {
          this.$notify.success({
            position: 'top-left',
            title: '提示',
            offset: 100,
            duration: 1000,
            message: _message
          });
        }
      }, wait_time);
    },
    // 3.用户提示信息
    user_tips: function user_tips(
      wait_time,
      wait_time2,
      message_type,
      _message
    ) {
      this.timer = setTimeout(() => {
        this.userConnectVisible = false;
      }, wait_time);
      this.timer = setTimeout(() => {
        if (message_type === MES_ERROR) {
          this.$notify.error({
            position: 'top-left',
            offset: 100,
            duration: 1000,
            title: '错误提示',
            message: _message
          });
        } else if (message_type === MES_INFO) {
          this.$notify.info({
            position: 'top-left',
            title: '提示',
            offset: 100,
            duration: 1000,
            message: _message
          });
        } else if (message_type === MES_SUCC) {
          this.$notify.success({
            position: 'top-left',
            title: '提示',
            offset: 100,
            duration: 1000,
            message: _message
          });
        }
      }, wait_time2);
    },
    // 4.进入聊天
    choseABot: function choseABot(index) {
      this.DrawVisible = true;
      ustore.set_bot(index);
      let history = [];
      history.push({
        pk: 0,
        username: ustore.state.botname.slice(8),
        text: defaultmessages[index - 1].text,
        pos: 1
      });
      console.log('Home history:', history);
      this.$refs.ctroom.getHistory(history);
    },
    // 4.注册
    toLogin: function toLogin(username, password) {
      console.log('signup');
      if (username.length > 20 || password.length > 20) {
        this.tips(0, MES_INFO, '用户名和密码最长为20个字符,请检查!');
        return;
      }
      // 注册并转到登录界面
      this.userConnectVisible = true;
      registerUser(username, password).then(
        Response => {
          if (Response.status === 200 && Response.data.code === 200) {
            // 信息传入后端，如是已注册用户则登陆成功，如果不是，alert显示用户名不存在，如果用户名存在，密码不存在，alert显示密码错误
            // 登录成功
            this.userConnectVisible = false;
            this.tips(0, MES_SUCC, '注册成功!');
            // 转到登录界面
            this.DialogVisible = 2;
          } else {
            this.user_tips(500, 500, MES_ERROR, '未知错误');
          }
        },
        error => {
          this.error_handle(error);
        }
      );
    },
    // 5.登录
    login: function login(username, password) {
      this.userConnectVisible = true;
      postUser(username, password).then(
        Response => {
          if (Response.status === 200 && Response.data.code === 200) {
            console.log('login successfully!');
            // 登录成功
            this.userConnectVisible = false;
            // TODO: 修改本地保存的用户数据
            let userinfo = {
              username: username
            };
            // 设置登录状态
            ustore.set_user(userinfo.username);
            ustore.set_online(true);
            localStore.save_json('userinfo', userinfo);

            this.tips(0, MES_SUCC, '登录成功!');
            this.DialogVisible = 0;
          } else {
            this.userConnectVisible = false;
            this.user_tips(500, 500, MES_ERROR, '未知错误');
          }
        },
        error => {
          this.userConnectVisible = false;
          this.error_handle(error);
        }
      );
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
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
.el-header {
  font-size: 200px Extra large;
  color: rgb(248, 242, 242);
  text-align: center;
  line-height: 600px;
}
#home {
  background: url("../assets/background.jpeg");
  width: 100%;
  height: 100%;
  position: fixed;
  background-size: 100% 100%;
}
</style>
