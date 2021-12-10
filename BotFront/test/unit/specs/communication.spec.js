import { sendMessage,registerUser,postUser,logOut,changePW,getHistory } from '@/utils/communications'

describe('UserStateStore.js', () => {
    it('sendMessage', () => {
      sendMessage("hello",1)
    }),
    it('registerUser', () => {
      registerUser("hello",'1')
    }),
    it('postUser', () => {
      postUser("hello",'1')
    }),
    it('logOut', () => {
      logOut()
    }),
    it('changePassWd', () => {
      changePW("hello", "1", "2")
    }),
    it('viewHistory', () => {
      getHistory("hello")
    })
})