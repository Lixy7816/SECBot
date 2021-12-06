import ChatRoom from '@/components/ChatRoom'
import { mount } from '@vue/test-utils'
import Vue from 'vue'

describe('ChatRoom.vue', () => {
  var vm;
  it('测试props default', () => {
    const Constructor = Vue.extend(ChatRoom)
    const ChatRoomComponent = new Constructor({}).$mount()
    expect(ChatRoomComponent.chatlist).toBeDefined()
  })
  it('测试无输入的send', () => {
    // const wrapper = mount(ChatRoom)
    // vm = wrapper.vm
    // vm.send()
  })
  it('测试send', () => {
    // const wrapper = mount(ChatRoom)
    // expect(wrapper.contains('textarea.txtarea')).toBe(true)
    // vm = wrapper.vm
    // vm.send()
    // vm.$el.querySelector('#textarea').value = '你好'
    // expect(vm.$el.querySelector('#textarea').value).toBe('你好')

    // expect(wrapper.contains('button.send')).toBe(true)
    // const button1 = wrapper.find('button.send')
    // button1.trigger('send')
  })
  it('点击返回按钮', () => {
    const wrapper = mount(ChatRoom)
    expect(wrapper.contains('el-page-header.backhome')).toBe(true)
    const button = wrapper.find('el-page-header.backhome')
    button.trigger('back')
  })
})
