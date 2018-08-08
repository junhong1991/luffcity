<template>
    <div>
      <h1>课程列表</h1>
      <ul v-for="item in courseList">
        <li>{{ item.name }} <a href="/course/1/">点击购买</a></li>
      </ul>
    </div>
</template>

<script>
    export default {
        name: "course",
        data(){
          return {
            // courseList: [11,22,33]
            courseList: [
              {id:1, title: 'Python基础'},
              {id:2, title: 'Java基础'},
              {id:3, title: 'Js基础'},
              {id:4, title: 'C#基础'},
            ]
          }
        },
      mounted(){
          this.initCourse();
      },
      methods: {
          initCourse: function () {
            let that = this;
            // 向后台发送ajax请求
            console.log('开始发送请求');
            this.$axios.request({
              url: 'http://127.0.0.1:8000/api/v1/courses/',
              method: 'GET',
              responseType: 'json'
            }).then(function (arg) {
              // 成功之后
              if (arg.data.code === 1000){
                that.courseList = arg.data.data
                console.log(arg.data.data);
              } else {
                alert(arg.data.error);
              }
            }).catch(function (arg) {

            })
          }
      }
    }
</script>

<style scoped>

</style>
