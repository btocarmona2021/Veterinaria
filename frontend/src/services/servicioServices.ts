import api from './api'
import type { Servicio } from '@/Interfaces/servicioInterface'

export default {
  obtenerServicios() {
    return api.get('/servicios')
  },

  obtenerServicio(id: number) {
    return api.get(`/servicio/${id}`)
  },
  crearServicio(servicio: Servicio) {
    return api.post('/servicio', servicio)
  },

  eliminarServicio(id: number) {
    return api.delete(`/servicio/${id}`)
  },
  modificarServicio(id: number, servicio: Servicio) {
    return api.put(`/servicio/${id}`, servicio)
  },
}
