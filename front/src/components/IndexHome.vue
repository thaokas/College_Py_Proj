<template>
  <main>
    <div>
      <button @click="goToCheckin" class="custom-button">Check-In</button>
    </div>
    <div>
      <button @click="goToRegister" class="custom-button">Register</button>
    </div>
  </main>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

function goToRegister() {
  router.push('/register')
}

function goToCheckin() {
  router.push('/checkin')
}
</script>

<style scoped>
main {
  display: flex;
  justify-content: center;
  gap: 50px;
  margin-top: 20px;
}

.custom-button {
  background-color: #42b983; /* 绿色背景 */
  color: white; /* 白色文字 */
  border: none; /* 无边框 */
  padding: 15px 30px; /* 内边距 */
  font-size: 18px; /* 字体大小 */
  border-radius: 5px; /* 圆角 */
  cursor: pointer; /* 鼠标悬停时显示为指针 */
  transition: background-color 0.3s ease, transform 0.3s ease; /* 过渡效果 */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 阴影 */
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.custom-button:hover {
  background-color: #38a169; /* 悬停时的绿色 */
  transform: translateY(-2px); /* 悬停时稍微上移 */
}

.custom-button:active {
  background-color: #2f855a; /* 按下时的绿色 */
  transform: translateY(0); /* 按下时恢复原位 */
}

.router-view {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
