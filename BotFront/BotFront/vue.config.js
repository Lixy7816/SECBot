module.exports = {
  devServer: {
    proxy: {
      '/chat':{
        target: 'http://localhost:8000',
        changOrigin: true
      },
      '/usermanager': {
        target: 'http://localhost:8000',
        changOrigin: true
      }
    }
  }
}
