import { localStore,STORAGE_KEY,get_token } from '@/store/StorageLocal'

describe('StorageLocal.js', () => {
    it('STORAGE_KEY', () => {
      expect(STORAGE_KEY).toEqual('lixy-15asf8f8wf1sdhg8j')
    }),
    it('localStore', () => {
        let json = {};
        let item = "hello";
        localStore.save_json(item,json);
        localStore.get_json(item);
        localStore.remove_json(item);
        expect(get_token('')).toBe('');
        get_token('token=aodfjaoifja');
    })
})