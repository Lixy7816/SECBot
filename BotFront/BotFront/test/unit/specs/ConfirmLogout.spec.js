import ConfirmLogout from '@/components/ConfirmLogout'
import { mount } from '@vue/test-utils'

describe('ConfirmLogout.vue', () => {
  it('点击确认添加按钮', () => {
    const wrapper = mount(ConfirmLogout)
    // confirm
    expect(wrapper.contains('el-button.confirm')).toBe(true)
    const button = wrapper.find('el-button.confirm')
    button.trigger('click')
  })
  it('点击取消按钮', () => {
    const wrapper = mount(ConfirmLogout)
    // cancel

    expect(wrapper.contains('el-button.cancel')).toBe(true)
    const button1 = wrapper.find('el-button.cancel')
    button1.trigger('click')
  })
})
