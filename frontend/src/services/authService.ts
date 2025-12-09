import api from './api'
import type { AuthUser } from '../Interfaces/authUser'

export default {
  login(authUser: AuthUser) {
    const datos_ingreso = {
      email: authUser.email,
      password: authUser.password,
    }
    return api.post('/login',datos_ingreso)
  },
}

