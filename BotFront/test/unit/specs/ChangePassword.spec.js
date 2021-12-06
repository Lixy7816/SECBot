import ChangePassword from '@/components/ChangePassword'
import { mount } from '@vue/test-utils'

describe('ChangePassword.vue', () => {
  it('确认修改->修改失败', () => {
    const wrapper = mount(ChangePassword)
    // confirm
    expect(wrapper.contains('el-button.confirm')).toBe(true)
    const button = wrapper.find('el-button.confirm')
    button.trigger('click')
  })
  it('确认修改->修改成功', () => {
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
  it('取消', () => {
    const wrapper = mount(ChangePassword)
    // cancel
    expect(wrapper.contains('el-form')).toBe(true)
    wrapper.vm.cancel()
  })
})
