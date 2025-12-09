import { defineStore } from 'pinia'
import type { AuthUser } from '@/Interfaces/authUser'
import { ref } from 'vue'
import authService from '@/services/authService'
import router from '@/router'

const useAuthStore = defineStore('auth',() => {
    const usuarioAutorizado = ref<AuthUser>({
      id: 0,
      email: '',
      jwt: '',
      rol: '',
      message: '',
    })
    const estaAutorizado = ref(false)

    async function login(authUser: AuthUser) {
      try {
        const response = await authService.login(authUser)
        usuarioAutorizado.value = response.data

        estaAutorizado.value = true
      } catch (error: any) {
        usuarioAutorizado.value = error.response.data
      }
    }

    function logout() {
      usuarioAutorizado.value = {
        id: 0,
        email: '',
        jwt: '',
        rol: '',
        message: '',
      }
      estaAutorizado.value = false
      router.push('/auth/login')
    }

    return { usuarioAutorizado, estaAutorizado, login, logout }
  },
  {
    persist: false,
  },
)
export default useAuthStore
