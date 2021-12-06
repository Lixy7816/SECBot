import { ustore,botnames } from '@/store/UserStateStore'

describe('UserStateStore.js', () => {
    it('botname', () => {
      expect(botnames).toEqual([
        'SECBot-小闲',
        'SECBot-小诗',
        'SECBot-小问',
        'SECBot-小影'
      ])
    }),
    it('ustore', () => {
        expect(ustore.state).toEqual({
            username: 'Lixy',
            botname: '小闲',
            botindex: 0,
            online: false
        })
        ustore.set_user('Xiang')
        ustore.set_bot(2)
        ustore.set_online(true)
        expect(ustore.state).toEqual({
            username: 'Xiang',
            botname: 'SECBot-小诗',
            botindex: 1,
            online: true
        })
        ustore.set_bot(8)
    })
})