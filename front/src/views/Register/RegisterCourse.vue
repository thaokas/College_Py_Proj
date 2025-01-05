<template>
  <div class="register-form">
    <h1>注册课程</h1>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="courseId">课程编号:</label>
        <input type="text" id="courseId" v-model="courseId" required />
      </div>
      <div class="form-group">
        <label for="courseName">课程名称:</label>
        <input type="text" id="courseName" v-model="courseName" required />
      </div>
      <div class="form-group">
        <label for="courseInfo">课程信息:</label>
        <textarea id="courseInfo" v-model="courseInfo" required></textarea>
      </div>
      <button type="submit" class="submit-button">提交</button>
    </form>
    <div v-if="message" class="message">
      <p>{{ message }}</p>
      <button @click="goToHome" class="home-button">返回首页</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'RegisterCourse',
  setup() {
    const courseId = ref('')
    const courseName = ref('')
    const courseInfo = ref('')
    const message = ref('')
    const router = useRouter()

    const submitForm = async () => {
      if (!courseId.value || !courseName.value || !courseInfo.value) {
        message.value = '请填写所有字段'
        return
      }

      const formData = new FormData()
      formData.append('courseId', courseId.value)
      formData.append('courseName', courseName.value)
      formData.append('courseInfo', courseInfo.value)

      try {
        const response = await axios.post('/api/register/course', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        message.value = '注册课程成功: ' + response.data.message
      } catch (error) {
        console.error('注册课程失败:', error)
        message.value = '注册课程失败'
      }
    }

    const goToHome = () => {
      router.push('/')
    }

    return {
      courseId,
      courseName,
      courseInfo,
      message,
      submitForm,
      goToHome
    }
  }
})
</script>

<style scoped>
.register-form {
  max-width: 600px;
  width:  calc(400px);
  padding: 30px;
  border: 1px solid #42b983;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  transition: transform 0.3s ease;
}

h1 {
  text-align: center;
  color: #1a202c;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #4a5568;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
  color: #1a202c;
  border: 1.5px solid #bcc4ce;
  border-radius: 5px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

input[type="text"]:focus,
textarea:focus {
  border-color: #42b983;
  box-shadow: 0 0 0 3px rgba(66, 185, 131, 0.5);
  outline: none;
}

.submit-button {
  width: 100%;
  padding: 12px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.submit-button:hover {
  background-color: #38a169;
  transform: translateY(-2px);
}

.submit-button:active {
  background-color: #2f855a;
  transform: translateY(0);
}

.message {
  margin-top: 20px;
  text-align: center;
}

.message p {
  color: #1a202c;
  margin-bottom: 10px;
}

.home-button {
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.home-button:hover {
  background-color: #38a169;
  transform: translateY(-2px);
}

.home-button:active {
  background-color: #2f855a;
  transform: translateY(0);
}
</style>
