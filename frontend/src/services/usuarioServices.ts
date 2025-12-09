import type { Usuario } from '@/Interfaces/usuarioInterface'
import api from './api'

export default {
  obtenerUsuarios() {
    return api.get('/usuarios')
  },

  obtenerUsuario(id: number) {
    return api.get(`/usuarios/${id}`)
  },

  crearUsuario(usuario: Usuario) {
    return api.post('/usuarios', usuario)
  },
  eliminarUsuario(id: number) {
    return api.delete(`/usuarios/${id}`)
  },
  modificarUsuario(id: number, usuario: Usuario) {
    return api.put(`/usuarios/${id}`, usuario)
  }
}
