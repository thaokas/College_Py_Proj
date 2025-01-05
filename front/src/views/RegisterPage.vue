<template>
  <div class="register-page">
    <h1 class="title">Register Page</h1>
    <div class="button-container">
      <button @click="goToRegisterStudent" class="register-button">Register Student</button>
      <button @click="goToRegisterCourse" class="register-button">Register Course</button>
      <button @click="goToSelectCourse" class="register-button">Enrollment</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'RegisterPage',
  setup() {
    const router = useRouter()

    const goToRegisterStudent = () => {
      router.push({ name: 'RegisterStudent' })
    }

    const goToRegisterCourse = () => {
      router.push({ name: 'RegisterCourse' })
    }

    const goToSelectCourse = () => {
      router.push({ name: 'SelectCourse' })
    }

    return {
      goToRegisterStudent,
      goToRegisterCourse,
      goToSelectCourse
    }
  }
})
</script>

<style scoped>
.register-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #383838;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  padding: 40px;
  border: 3px solid #387a3a; /* 绿色围边 */
  border-radius: 15px; /* 圆润边框 */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 添加阴影 */
}

.title {
  font-size: 2.5em;
  color: #97c002;
  margin-bottom: 30px;
  border-bottom: 3px solid #387a3a;
  padding-bottom: 10px;
  width: 100%;
  max-width: 400px;
  text-align: center;
}

.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.register-button {
  margin: 15px;
  padding: 12px 24px;
  font-size: 18px;
  cursor: pointer;
  border: none;
  border-radius: 8px;
  background: linear-gradient(135deg, #4caf50, #81c784); /* 绿色渐变 */
  color: white;
  transition: background 0.3s ease, transform 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.register-button:hover {
  background: linear-gradient(135deg, #81c784, #4caf50); /* 绿色渐变悬停效果 */
  transform: translateY(-2px);
}
</style>
