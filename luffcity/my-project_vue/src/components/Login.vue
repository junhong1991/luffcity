<template>
    <div>
      <h1>用户登录</h1>
      <input type="text" placeholder="用户名">
      <input type="text" placeholder="密码">
      <input type="button" value="提交" v-on:click="doLogin">
    </div>
</template>

<script>
    export default {
        name: "Login",
      data(){
          return {
            username: '',
            password: '',
          }
      },
      methods: {
          doLogin(){
            var that = this;
            // 向后台发送ajax氢气
            this.$axios.request({
              url: 'http://127.0.0.1:8000/api/vi/auth/',
              method: 'POST',
              data: {
                user: this.username,
                pwd: this.password,
              },
              headers: {
                'Content-Type':'application/json'
              },
              responseType: 'json'
            }).then(function (arg) {
              // 成功之后
              // if (arg.data.code === 1000){
              //   that.courseList = arg.data.data
              // }else {
              //   alert(arg.data.error)
              // }
            }).catch(function (arg) {

            })
          }
      }
    }
</script>

<style scoped>

</style>
