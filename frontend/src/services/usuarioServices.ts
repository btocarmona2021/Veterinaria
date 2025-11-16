import type { Usuario } from '@/Interfaces/usuarioInterface'
import api from './api'

export default {
  obtenerUsuarios() {
    return api.get('/usuarios')
  },

  obtenerUsuario(id: number) {
    return api.get(`/usuario/${id}`)
  },

  crearUsuario(usuario: Usuario) {
    return api.post('/usuario', usuario)
  },
  eliminarUsuario(id: number) {
    return api.delete(`/usuario/${id}`)
  },
  modificarUsuario(id: number, usuario: Usuario) {
    return api.put(`/usuario/${id}`, usuario)
  }
}
