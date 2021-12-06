const STORAGE_KEY = 'lixy-15asf8f8wf1sdhg8j'
export var localStore = {
  save_json (item, json) {
    window.localStorage.setItem(STORAGE_KEY + item, JSON.stringify(json))
  },
  get_json (item) {
    return JSON.parse(window.localStorage.getItem(STORAGE_KEY + item) || '[]')
  },
  remove_json (item) {
    window.localStorage.removeItem(STORAGE_KEY + item)
  }
}
