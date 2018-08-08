<template>
    <div>
      <ul v-for="item in courseList">
        <li>{{ item.name }} <a href="/course/1/">点击购买</a></li>
      </ul>
      <h1>课程详情</h1>
      <ul v-for="item in courseList">
        <li>{{ item.name }}</li>
        <p></p>
        <li>{{ item.what_to_study_brief}}</li>
        <p></p>
        <li>{{ item.why_study}}</li>
      </ul>
    </div>
</template>

<script>
    export default {
        name: "CourseDetail",
      data(){
        return {
          // courseList: [11,22,33]
          courseList: [ ]
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
            url: 'http://127.0.0.1:8000/api/v1/courses/1/',
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
