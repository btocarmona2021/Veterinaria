import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:3000', // <-- tu backend Flask
  headers: {
    'Content-Type': 'application/json',
  },
})

// Interceptor opcional para token (si luego agregas login)
// api.interceptors.request.use((config) => {
//   const token = localStorage.getItem('token')
//   if (token) {
//     config.headers.Authorization = `Bearer ${token}`
//   }
//   return config
// })

export default api
