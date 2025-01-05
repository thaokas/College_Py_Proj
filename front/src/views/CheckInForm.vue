<!-- src/views/CheckInForm.vue -->
<template>
  <div class="checkin-form">
    <h1>Check-In Page</h1>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="photo">Upload Check-In Photo:</label>
        <input type="file" id="photo" ref="photoInput" @change="handleFileChange" accept="image/*" required />
      </div>
      <div class="form-group">
        <label for="number">Enter Course Id:</label>
        <input type="number" id="number" v-model="formData.number" required />
      </div>
      <div class="form-group">
        <label for="text">Enter Course Name:</label>
        <input type="text" id="text" v-model="formData.text" required />
      </div>
      <button type="submit" class="submit-button">Submit</button>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export default defineComponent({
  name: 'CheckInForm',
  setup() {
    const router = useRouter()
    const photoInput = ref<HTMLInputElement | null>(null)
    const formData = ref({
      photo: null as File | null,
      number: '',
      text: ''
    })

    const handleFileChange = (event: Event) => {
      const target = event.target as HTMLInputElement
      if (target.files && target.files.length > 0) {
        formData.value.photo = target.files[0]
      }
    }

    const submitForm = async () => {
      if (!formData.value.photo || !formData.value.number || !formData.value.text) {
        alert('Please fill in all fields.')
        return
      }

      const formDataToSend = new FormData()
      formDataToSend.append('photo', formData.value.photo)
      formDataToSend.append('number', formData.value.number)
      formDataToSend.append('text', formData.value.text)

      try {
        const response = await axios.post('/api/checkin', formDataToSend, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        console.log('Success:', response.data)
        router.push({ name: "CheckInResult", state: { result : response.data}})
      } catch (error) {
        console.error('Error:', error)
        alert('Check-in failed. Please try again.')
      }
    }

    return {
      photoInput,
      formData,
      handleFileChange,
      submitForm
    }
  }
})
</script>

<style scoped>
.checkin-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  align-items: center;
}

h1 {
  text-align: center;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input[type="file"],
input[type="number"],
input[type="text"] {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.submit-button {
  width: 100%;
  padding: 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #38a169;
}

.submit-button:active {
  background-color: #2f855a;
}
</style>
