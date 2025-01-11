<script setup lang="ts">
import HelloWorld from './components/HelloWorld.vue'
import Index from './components/IndexHome.vue'
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<template>
  <header>
    <div class="wrapper">
      <HelloWorld msg="Welcome to Easy Checkin!" />
    </div>
  </header>

  <main>
    <Index v-if="route.path === '/'"/>
    <div class="router-view">
      <router-view ></router-view>
    </div>
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}

main {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

.custom-button {
  background-color: #42b983; /* 绿色背景 */
  color: white; /* 白色文字 */
  border: none; /* 无边框 */
  padding: 10px 20px; /* 内边距 */
  font-size: 16px; /* 字体大小 */
  border-radius: 5px; /* 圆角 */
  cursor: pointer; /* 鼠标悬停时显示为指针 */
  transition: background-color 0.3s ease, transform 0.3s ease; /* 过渡效果 */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 阴影 */
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
