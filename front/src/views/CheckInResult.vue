<!-- src/views/CheckInResult.vue -->
<template>
  <div class="checkin-result">
    <h1>Check-In Result</h1>
    <div v-if="result">
      <p><strong>Field 1:</strong> {{ result.field1 }}</p>
      <p><strong>Field 2:</strong> {{ result.field2 }}</p>
      <p><strong>Field 3:</strong> {{ result.field3 }}</p>
      <p><strong>Field 4:</strong> {{ result.field4 }}</p>
      <div>
        <h2>List 1</h2>
        <ul>
          <li v-for="(item, index) in result.list1" :key="index">{{ item }}</li>
        </ul>
      </div>
      <div>
        <h2>List 2</h2>
        <ul>
          <li v-for="(item, index) in result.list2" :key="index">{{ item }}</li>
        </ul>
      </div>
      <!-- 你可以根据返回的数据结构添加更多字段 -->
    </div>
    <div v-else>
      <p>No result available.</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

interface CheckInResult {
  field1: number;
  field2: number;
  field3: string;
  field4: string;
  list1: string[];
  list2: string[];
}

export default defineComponent({
  name: 'CheckInResult',
  setup() {
    const route = useRoute()
    const router = useRouter()
    const rawResult = route.params.result || route.query.result || null;

    // 尝试将结果解析为 JSON 对象
    let parsedResult: CheckInResult | null = null;
    if (typeof rawResult === 'string') {
      try {
        parsedResult = JSON.parse(rawResult);
      } catch (error) {
        console.error('Failed to parse result:', error);
      }
    } else if (rawResult && typeof rawResult === 'object') {
      parsedResult = rawResult as unknown as CheckInResult;
    }

    const result = ref<CheckInResult | null>(parsedResult);

    onMounted(() => {
      if (!result.value) {
        alert('No result found. Redirecting back to Check-In Form.')
        router.push({ name: 'CheckInForm' })
      }
    })

    return {
      result
    }
  }
})
</script>

<style scoped>
.checkin-result {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  align-items: center;
}

h1, h2 {
  text-align: center;
}

p {
  margin-bottom: 10px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 5px;
}
</style>
