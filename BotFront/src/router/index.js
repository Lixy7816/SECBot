import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/views/Home';
import ChatRoom from '@/views/ChatRoom';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      meta: {
        // 网页标题
        title: 'SECBot聊天区'
      }
    },
    {
      path: '/ChatRoom',
      name: 'ChatRoom',
      component: ChatRoom,
      meta: {
        // 网页标题
        title: 'SECBot聊天区'
      }
    },
  ],
});
