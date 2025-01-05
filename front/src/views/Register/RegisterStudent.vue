<template>
    <div class="register-form">
      <h1>注册学生</h1>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="studentId">学号:</label>
          <input type="text" id="studentId" v-model="studentId" required />
        </div>
        <div class="form-group">
          <label for="studentName">学生姓名:</label>
          <input type="text" id="studentName" v-model="studentName" required />
        </div>
        <div class="form-group">
          <label for="photo">照片:</label>
          <input type="file" id="photo" @change="handleFileUpload" accept="image/*" required />
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
  name: 'RegisterStudent',
  setup() {
    const studentId = ref('')
    const studentName = ref('')
    const photo = ref<File | null>(null)
    const message = ref('')
    const router = useRouter()

    const handleFileUpload = (event: Event) => {
      const target = event.target as HTMLInputElement
      if (target.files && target.files.length > 0) {
        photo.value = target.files[0]
      }
    }

    const submitForm = async () => {
      if (!studentId.value || !studentName.value || !photo.value) {
        message.value = '请填写所有字段并上传照片'
        return
      }

      const formData = new FormData()
      formData.append('studentId', studentId.value)
      formData.append('studentName', studentName.value)
      formData.append('photo', photo.value)

      try {
        const response = await axios.post('/api/register/student', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        message.value = '请求成功: ' + response.data.message
      } catch (error) {
        console.error('POST请求发送失败:', error)
        message.value = '请求失败'
      }
    }

    const goToHome = () => {
      router.push('/')
    }

    return {
      studentId,
      studentName,
      photo,
      message,
      handleFileUpload,
      submitForm,
      goToHome
    }
  }
})
</script>

<style scoped>
.register-form {
  max-width: 400px;
  width: 100%;
  padding: 30px;
  border: px solid #42b983;
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
input[type="number"],
input[type="file"] {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
  color: #1a202c;
  border: 1.5px solid #bcc4ce;
  border-radius: 5px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

input[type="text"]:focus,
input[type="number"]:focus,
input[type="file"]:focus {
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
