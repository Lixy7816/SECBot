import Vue from "vue";
import Home from "@/views/Home";

describe("Home.vue", () => {
  it("should render correct contents", () => {
    const Constructor = Vue.extend(Home);
    const vm = new Constructor().$mount();
  });
  it("Test error handle", () => {
    const Constructor = Vue.extend(Home);
    const vm = new Constructor().$mount();
    let error1 = {
      respnose: ""
    };
    vm.error_handle(error1);
    let error2 = {
      respnose: {
        status: 400,
        data: {
          data: "hello"
        }
      }
    };
    vm.error_handle(error2);
    let error3 = {
      respnose: {
        status: 401,
        data: {
          data: "hello"
        }
      }
    };
    vm.error_handle(error3);
    let error4 = {
      respnose: {
        status: 405,
        data: {
          data: "hello"
        }
      }
    };
    vm.choseABot(0);
    vm.error_handle(error4);
    vm.tips(0, 0, "");
    vm.tips(0, 1, "");
    vm.tips(0, 2, "");
    vm.user_tips(0, 0, 0, "");
    vm.user_tips(0, 0, 1, "");
    vm.user_tips(0, 0, 2, "");
    vm.setUserState('请登录',true);
    vm.setUserState('请登录',false);
    let historys1 = [
      {
        query: 'hello',
        answer: 'world',
        bot_id: 0,
        timestamp: 0
      },
      {
        query: 'hello',
        answer: 'world',
        bot_id: 0,
        timestamp: 0
      }
    ];
    vm.processHistorys(historys1);

  });
});
