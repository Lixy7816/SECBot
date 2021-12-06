import ChatBox from '@/components/ChatBox'
import Vue from 'vue'

describe('ChatBox.vue', () => {
  it('测试props default', () => {
    const Constructor = Vue.extend(ChatBox)
    const ChatBoxComponent = new Constructor({}).$mount()
    expect(ChatBoxComponent.username).toBe('username')
    expect(ChatBoxComponent.text).toBe('hello world')
    expect(ChatBoxComponent.pos).toBe(2)
  })
})
