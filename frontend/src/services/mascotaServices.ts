import api from "./api";
import type { Mascota } from "@/Interfaces/mascotaInterface";

export default {
  obtenerMascotas() {
    return api.get('/mascotas')
  },
  obtenerMascotasFront() {
    return api.get('/mascotasfront')
  },

  obtenerMascota(id: number) {
    return api.get(`/mascotas/${id}`)
  },

  crearMascota(mascota: Mascota) {
    return api.post('/mascotas', mascota)
  },

  eliminarMascota(id: number) {
    return api.delete(`/mascotas/${id}`)
  },
  modificarMascota(id: number, mascota: Mascota) {
    return api.put(`/mascotas/${id}`, mascota)
  },
}


