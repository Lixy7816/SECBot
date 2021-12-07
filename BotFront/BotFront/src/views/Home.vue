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
            v-if="ustate.online"
            index="3"
            v-on:click="DialogVisible = 3"
            class="changePw"
            >修改密码</el-menu-item
          >
          <el-menu-item
            v-if="ustate.online"
            index="4"
            v-on:click="DialogVisible = 4"
            class="logout"
            >退出登录</el-menu-item
          >
          <el-menu-item index="5">{{ ustate.username }}</el-menu-item>
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
      <ChatRoom ref="ctroom" v-on:back="DrawVisible = false" />
    </el-drawer>
  </div>
</template>

<script>
import {
  registerUser,
  postUser,
  changePW,
  logOut,
  getHistory
} from '@/utils/communications';
import { ustore } from '@/store/UserStateStore';
import { hstore } from '@/store/HistoryStore';
import { localStore, get_token } from '@/store/StorageLocal';
import Signup from '@/components/Signup';
import Login from '@/components/Login';
import ConfirmLogout from '@/components/ConfirmLogout';
import ChangePw from '@/components/ChangePassword';
import ChooseBot from '@/components/ChooseBot';
import ChatRoom from '@/components/ChatRoom';

let MES_INFO = 0;
let MES_ERROR = 1;
let MES_SUCC = 2;
let USER_ERROR_INFO = '用户未登录或登录信息已过期,请重新登录';
let UNKNOWN_ERROR_INFO = '发生未知异常,请检查网络连接或联系开发人员';

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
      DialogVisible: 0,
      DrawVisible: false,
      loadingVisible: false,
      userConnectVisible: false,
      dialogVisible_logout: false,
      ustate: ustore.state
    };
  },
  methods: {
    // 1.错误处理代码
    error_handle: function error_handle(error) {
      console.log(error);
      let respnose = error.response;
      if (
        typeof respnose === 'undefined' ||
        typeof respnose.status === 'undefined'
      ) {
        // 1.1 未知错误1
        this.user_tips(500, 500, MES_ERROR, UNKNOWN_ERROR_INFO);
      } else if (respnose.status === 400) {
        // 1.2 通用错误信息
        let data = respnose.data.data;
        this.user_tips(0, 0, MES_ERROR, data);
      } else if (respnose.status === 401) {
        // 1.3 用户未登录或登录过期问题
        this.user_tips(0, 0, MES_ERROR, USER_ERROR_INFO);
        // 后端反馈登录状态过期,则前端需清除用户相关信息
        ustore.set_online(false);
        ustore.set_user('请登录');
        this.DialogVisible = 0;
        localStore.remove_json('userinfo');
      } else {
        // 1.4 未知错误信息2
        this.user_tips(400, 400, MES_ERROR, UNKNOWN_ERROR_INFO);
      }
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
      if (!ustore.state.online) {
        this.tips(0, MES_INFO, '请先登录~');
        return;
      }
      this.DrawVisible = true;
      ustore.set_bot(index);

      // console.log('Home history:', hstore.state[index - 1]);
      this.$refs.ctroom.getHistory(hstore.state[index - 1]);
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
            let userinfo = {
              username: username
            };
            // 设置登录状态
            ustore.set_user(userinfo.username);
            ustore.set_online(true);
            localStore.save_json('userinfo', userinfo);

            this.tips(0, MES_SUCC, '登录成功!');

            // 登录后读取历史记录
            hstore.clear();
            hstore.add_default_message();
            getHistory(ustore.state.username).then(
              Response2 => {
                if (Response2.status === 200 && Response2.data.code === 200) {
                  let historys = Response2.data.data;
                  for (let i = 0; i < historys.length; i += 1) {
                    hstore.add_historys(historys[i]);
                  }
                } else {
                  this.tips(500, 500, MES_ERROR, '获取历史记录失败');
                }
              },
              error => {
                this.error_handle(error);
              }
            );
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
    },
    // 6.修改密码
    changepassword: function changepassword(password, new_password) {
      this.userConnectVisible = true;
      changePW(this.ustate.username, password, new_password).then(
        Response => {
          if (Response.status === 200 && Response.data.code === 200) {
            // 密码修改成功成功
            this.userConnectVisible = false;
            this.tips(0, MES_SUCC, '密码修改成功!');
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
    },
    // 7. 退出登录
    logout: function logout() {
      logOut().then(
        Response => {
          if (Response.status === 200 && Response.data.code === 200) {
            // 退出成功
            ustore.set_online(false);
            ustore.set_user('请登录');
            this.DialogVisible = 0;
            localStore.remove_json('userinfo');
            this.tips(100, MES_INFO, '已退出登录');
          } else {
            this.user_tips(500, 500, MES_ERROR, '未知错误');
          }
        },
        error => {
          this.error_handle(error);
        }
      );
    }
  },
  created() {
    // 初始化时从本地存储读取用户信息,若存在用户信息但cookie中的token已过期,则退出登录并删除数据
    let userinfo = localStore.get_json('userinfo');
    if (typeof userinfo.username !== 'undefined') {
      ustore.set_user(userinfo.username);
      ustore.set_online(true);
      let uname = get_token(document.cookie);
      if (uname === '') {
        ustore.set_online(false);
        ustore.set_user('请登录');
        this.DialogVisible = 0;
        localStore.remove_json('userinfo');
        this.$alert('会话已过期,请重新登录', '提示', {
          confirmButtonText: '确定'
        });
      }
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
