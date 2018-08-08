import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Course from '@/components/Course'
import News from '@/components/News'
import Login from '@/components/Login'
import CourseDetail from '@/components/CourseDetail'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/course',
      name: 'course',
      component: Course
    },
    {
      path: '/news',
      name: 'news',
      component: News
    },
    {
      path: '/login',
      name: 'news',
      component: Login
    },
    {
      path: '/course/1/',
      name: 'courseDetail',
      component: CourseDetail
    }
  ]
})
