import api from './api'
import type { Servicio } from '@/Interfaces/servicioInterface'

export default {
  obtenerServicios() {
    return api.get('/servicios')
  },

  obtenerServicio(id: number) {
    return api.get(`/servicios/${id}`)
  },
  crearServicio(servicio: Servicio) {
    return api.post('/servicios', servicio)
  },

  eliminarServicio(id: number) {
    return api.delete(`/servicios/${id}`)
  },
  modificarServicio(id: number, servicio: Servicio) {
    return api.put(`/servicios/${id}`, servicio)
  },
}
