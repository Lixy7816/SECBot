import { sort, reverse, unique } from '@/utils/DataProcess'

describe('DataProcess.js', () => {
    it('sort', () => {
      let array = [1,2,3,5,4];
      let res = sort(array);
      expect(res).toEqual([1,2,3,4,5])
    }),
    it('reverse', () => {
        let array = [1,2,3,4,5];
        let res = reverse(array);
        expect(res).toEqual([5,4,3,2,1])
    })
    it('unique', () => {
        let array = [1,2,3,4,5,1,1];
        let res = unique(array);
        expect(res).toEqual([1,2,3,4,5])
    })
})