import { mount } from '@vue/test-utils'
import Login from '@/components/Login'

describe('Login.vue', () => {
  it('跳转至注册页面', () => {
    const wrapper = mount(Login)

    expect(wrapper.contains('el-button')).toBe(true)
    wrapper.find('el-button.signup').trigger('click')

    expect(wrapper.emitted()).toEqual({'signup': [[]]})
  })
  it('确认登录', () => {
    const wrapper = mount(Login)
    expect(wrapper.contains('el-button.confirm')).toBe(true)
    wrapper.find('el-button.confirm').trigger('click')
    expect(wrapper.confirm).toEqual()
  })
  it('取消登录', () => {
    const wrapper = mount(Login)
    expect(wrapper.contains('el-button.cancel')).toBe(true)
    wrapper.find('el-button.cancel').trigger('click')
    expect(wrapper.cancel).toEqual()
  })
  it('点击确认按钮', () => {
    const wrapper = mount(Login)
    // cancel
    wrapper.setData({ruleForm: {
      username: 'fyc',
      password: '123'
    }})
    expect(wrapper.contains('el-form')).toBe(true)
    const button = wrapper.find('el-button.confirm')
    button.trigger('click')
    // wrapper.vm.confirm('ruleForm')
  })
})
