import { mount } from '@vue/test-utils'
import Signup from '@/components/Signup'

describe('Signup.vue', () => {
  it('取消注册', () => {
    const wrapper = mount(Signup)

    expect(wrapper.contains('el-button')).toBe(true)
    wrapper.find('el-button.cancel').trigger('click')

    expect(wrapper.emitted()).toEqual({'cancel': [[]]})
  })
  it('确认注册', () => {
    const wrapper = mount(Signup)

    expect(wrapper.contains('el-button.confirm')).toBe(true)
    wrapper.find('el-button.confirm').trigger('click')

    expect(wrapper.confirm).toEqual()
  })
  it('密码一致', () => {
    const wrapper = mount(Signup)
    wrapper.setData({ruleForm: {password2: '12345'}})
    wrapper.setData({ruleForm: {
      password: '123'
    }})
  })
  it('点击确认按钮', () => {
    const wrapper = mount(Signup)
    // cancel
    wrapper.setData({ruleForm: {
      username: 'fyc',
      password: '123'
    }})
    wrapper.setData({ruleForm: {
      password2: '1234'
    }})
    expect(wrapper.contains('el-form')).toBe(true)
    const button = wrapper.find('el-button.confirm')
    button.trigger('click')
  })
})
