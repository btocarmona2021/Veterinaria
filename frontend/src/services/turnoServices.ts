import api from './api'
import type { Turno } from '@/Interfaces/turnoInterface'

export default {
  obtenerTurnos() {
    return api.get('/turnos')
  },

  obtenerTurno(id: number) {
    return api.get(`/turno/${id}`)
  },

  crearTurno(turno: Turno) {
    return api.post('/turno', turno)
  },

  eliminarTurno(id: number) {
    return api.delete(`/turno/${id}`)
  },
  modificarTurno(id: number, turno: Turno) {
    return api.put(`/turno/${id}`, turno)
  },
}
