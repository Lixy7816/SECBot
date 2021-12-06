import ChangePassword from '@/components/ChangePassword'
import { mount } from '@vue/test-utils'

describe('ChangePassword.vue', () => {
  it('点击确认添加按钮', () => {
    const wrapper = mount(ChangePassword)
    // confirm
    expect(wrapper.contains('el-button.confirm')).toBe(true)
    const button = wrapper.find('el-button.confirm')
    button.trigger('click')
  })
  it('点击取消按钮', () => {
    const wrapper = mount(ChangePassword)
    // cancel
    wrapper.setData({ruleForm: {
      password: '123'
    }})
    wrapper.setData({ruleForm: {
      password2: '1234'
    }})
    expect(wrapper.contains('el-form')).toBe(true)
    const button = wrapper.find('el-button.confirm')
    button.trigger('click')
  })
  it('点击取消按钮', () => {
    const wrapper = mount(ChangePassword)
    // cancel
    expect(wrapper.contains('el-form')).toBe(true)

    expect(wrapper.contains('el-button.cancel')).toBe(true)
    const button1 = wrapper.find('el-button.cancel')
    button1.trigger('click')
  })
})
