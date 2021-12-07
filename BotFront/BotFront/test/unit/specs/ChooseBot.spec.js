import ChooseBot from '@/components/ChooseBot'
import { mount } from '@vue/test-utils'

describe('ChooseBot.vue', () => {
  it('测试props default', () => {
    const wrapper = mount(ChooseBot)
    wrapper.vm.chooseABot(3)
  })
})
