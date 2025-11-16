import api from "./api";
import type { Mascota } from "@/Interfaces/mascotaInterface";

export default {
  obtenerMascotas() {
    return api.get('/mascotas')
  },

  obtenerMascota(id: number) {
    return api.get(`/mascota/${id}`)
  },

  crearMascota(mascota: Mascota) {
    return api.post('/mascota', mascota)
  },

  eliminarMascota(id: number) {
    return api.delete(`/mascota/${id}`)
  },
  modificarMascota(id: number, mascota: Mascota) {
    return api.put(`/mascota/${id}`, mascota)
  },
}


