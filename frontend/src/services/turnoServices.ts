import api from './api'
import type { Turno } from '@/Interfaces/turnoInterface'

export default {
  obtenerTurnos() {
    return api.get('/turnos')
  },

  obtenerTurno(id: number) {
    return api.get(`/turnos/${id}`)
  },

  crearTurno(turno: Turno) {
    return api.post('/turnos', turno)
  },

  eliminarTurno(id: number) {
    return api.delete(`/turnos/${id}`)
  },
  modificarTurno(id: number, turno: Turno) {
    return api.put(`/turnos/${id}`, turno)
  },
}
