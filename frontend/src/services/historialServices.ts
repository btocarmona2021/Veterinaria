import api from "./api";
import type { Historial } from "@/Interfaces/historialInterface";

export default {
  obtenerHistoriales() {
    return api.get('/historial')
  },

  obtenerHistorial(id: number) {
    return api.get(`/historial/${id}`)
  },

  crearHistorial(historial: Historial) {
    return api.post('/historial', historial)
  },

  eliminarHistorial(id: number) {
    return api.delete(`/historial/${id}`)
  },
  modificarHistorial(id: number, historial: Historial) {
    return api.put(`/historial/${id}`, historial)
  },
}
