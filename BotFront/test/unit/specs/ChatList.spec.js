import ChatList from '@/components/ChatList'
import Vue from 'vue'

describe('ChatList.vue', () => {
  it('测试props default', () => {
    const Constructor = Vue.extend(ChatList)
    const ChatListComponent = new Constructor({}).$mount()
    expect(ChatListComponent.chatList).toBeDefined()
  })
})
