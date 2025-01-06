// src/router/index.ts
import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import Register from '../views/RegisterPage.vue'
import Checkin from '../views/CheckInForm.vue'
import CheckInResult from '../views/CheckInResult.vue'
import RegisterStudent from '../views/Register/RegisterStudent.vue'
import RegisterCourse from '../views/Register/RegisterCourse.vue'
import SelectCourse from '../views/Register/CourseEnrollment.vue'

const routes: Array<RouteRecordRaw> = [
  { path: '/register', component: Register },
  { path: '/checkin', component: Checkin },
  { path: '/checkin/result', component: CheckInResult, name: 'CheckInResult' },
  { path: '/register/student', component: RegisterStudent, name: 'RegisterStudent' },
  { path: '/register/course', component: RegisterCourse, name: 'RegisterCourse' },
  { path: '/register/enrollment', component: SelectCourse, name: 'SelectCourse' },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
