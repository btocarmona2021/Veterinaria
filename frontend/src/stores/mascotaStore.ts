// stores/mascotaStore.ts
import { defineStore } from 'pinia'
import mascotaServices from '@/services/mascotaServices'
import type { Mascota } from '@/Interfaces/mascotaInterface'

export const useMascotaStore = defineStore('mascotaStore', {
  state: () => ({
    mascotas: [] as Mascota[],
    mascota: null as Mascota | null,
    cargando: false as boolean,
    error: null as string | null,
  }),

  actions: {
    async obtenerMascotas() {
      try {
        this.cargando = true
        const res = await mascotaServices.obtenerMascotas()
        this.mascotas = res.data
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async obtenerMascota(id: number) {
      try {
        this.cargando = true
        const res = await mascotaServices.obtenerMascota(id)
        this.mascota = res.data
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async crearMascota(data: Mascota) {
      try {
        this.cargando = true
        const res = await mascotaServices.crearMascota(data)
        this.mascotas.push(res.data)
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async modificarMascota(id: number, data: Mascota) {
      try {
        this.cargando = true
        const res = await mascotaServices.modificarMascota(id, data)

        const index = this.mascotas.findIndex((m) => m.id === id)
        if (index !== -1) this.mascotas[index] = res.data
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async eliminarMascota(id: number) {
      try {
        this.cargando = true
        await mascotaServices.eliminarMascota(id)

        this.mascotas = this.mascotas.filter((m) => m.id !== id)
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },
  },
})
