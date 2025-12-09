import axios from 'axios'
import useAuthStore from '@/stores/authStore'

const api = axios.create({
  baseURL: 'http://localhost:3000/api_v1',
  headers: {
    'Content-Type': 'application/json',
  },
})

// Interceptor token
api.interceptors.request.use((config) => {
  const authStore = useAuthStore()

  if (authStore.usuarioAutorizado.jwt) {
    config.headers.Authorization = `Bearer ${authStore.usuarioAutorizado.jwt}`
  }

  return config
})

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      const usuarioStore = useAuthStore()
      usuarioStore.logout()
    }

    return Promise.reject(error)
  },
)

export default api
