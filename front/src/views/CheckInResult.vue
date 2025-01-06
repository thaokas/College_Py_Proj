<!-- src/views/CheckInResult.vue -->
<template>
  <div class="checkin-result-card">
    <h1>Check-In Result</h1>
    <div v-if="result && result.request_result === 'SUCCESS'" class="result-content">
      <div class="result-item">
        <strong>课堂共到来:</strong> {{ result.all_attendance_num }} <strong>人</strong>
      </div>
      <div class="result-item">
        <strong>正常出勤:</strong> {{ result.attendance_num }} <strong>人</strong>
      </div>
      <div class="result-item">
        <strong>缺勤:</strong> {{ result.absent_num }} <strong>人</strong>
      </div>
      <div class="result-item">
        <strong>非本课堂学生:</strong> {{ result.unknown_num }} <strong>人</strong>
      </div>
      <div class="list-container">
        <div class="list-item" v-if="result.absent_students_list.length > 0">
          <h2>缺勤学生名单</h2>
          <ol>
            <li
              v-for="(item, index) in result.absent_students_list"
              :key="item.uid"
              @click="toggleShowUid(item.uid)"
            >
              {{ showUid[item.uid] ? item.uid : item.name }}
            </li>
          </ol>
        </div>
        <div class="list-item" v-if="result.unknown_students_list.length > 0">
          <h2>非本课堂学生名单</h2>
          <ol>
            <li
              v-for="(item, index) in result.unknown_students_list"
              :key="item.uid"
              @click="toggleShowUid(item.uid)"
            >
              {{ showUid[item.uid] ? item.uid : item.name }}
            </li>
          </ol>
        </div>
      </div>
    </div>
    <div v-else class="no-result">
      <p>No result available.</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, reactive } from 'vue'
import { useRoute, useRouter } from 'vue-router'

export default defineComponent({
  name: 'CheckInResult',

  setup() {
    const route = useRoute()
    const router = useRouter()
    const showUid = reactive({}) as { [key: string]: boolean }

    let result = null
    try {
      result = JSON.parse(decodeURIComponent(route.params.result))
    } catch (error) {
      console.error('Error parsing result:', error)
      alert('Failed to parse result. Redirecting back to Check-In Form.')
      router.push({ name: 'CheckInForm' })
      return {} // 确保返回空对象以避免后续错误
    }

    // 确保 absent_students_list 和 unknown_students_list 中的每个对象都被正确解析
    if (result && result.absent_students_list) {
      result.absent_students_list = result.absent_students_list.map(item => {
        try {
          return JSON.parse(item)
        } catch (error) {
          console.error('Error parsing absent_students_list item:', error)
          return item
        }
      })
    }

    if (result && result.unknown_students_list) {
      result.unknown_students_list = result.unknown_students_list.map(item => {
        try {
          return JSON.parse(item)
        } catch (error) {
          console.error('Error parsing unknown_students_list item:', error)
          return item
        }
      })
    }

    const toggleShowUid = (uid: string) => {
      showUid[uid] = !showUid[uid]
    }

    return {
      result,
      showUid,
      toggleShowUid
    }
  }
})
</script>

<style scoped>
.checkin-result-card {
  background-color: #e8f5e9;
  border-radius: 16px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 30px;
  width: 400px;
  max-width: 600px;
  text-align: center;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #333;
  font-weight: bold;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

.result-content {
  text-align: center;
}

.result-item {
  margin-bottom: 15px;
  font-size: 16px;
  color: #333;
}

.result-item strong {
  color: #4caf50; /* Green color for strong text */
}

.no-result {
  margin-top: 20px;
  font-size: 18px;
  color: #999;
}

.list-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 20px;
  align-items: start;
}

.list-item {
  width: 48%;
  text-align: left;
  margin: 0 1%;
  color: #333;
  align-content: center;
  text-align: center;
}

.list-item h2 {
  font-size: 18px;
  margin-bottom: 10px;
  text-align: center;
  color: #4caf50; /* Green color for headings */
}

ol {
  list-style-type: none;
  padding: 0;
}

li {
  background-color: #f9f9f9;
  border: 1px solid #c8e6c9; /* Light green border */
  border-radius: 4px;
  padding: 8px;
  margin-bottom: 5px;
  transition: background-color 0.3s ease;
  cursor: pointer; /* 显示为指针 */
}

li:hover {
  background-color: #e0f7fa; /* Lighter green on hover */
}
</style>
