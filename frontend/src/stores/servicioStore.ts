// stores/servicioStore.ts
import { defineStore } from 'pinia'
import servicioServices from '@/services/servicioServices'
import type { Servicio } from '@/Interfaces/servicioInterface'

export const useServicioStore = defineStore('servicioStore', {
  state: () => ({
    servicios: [] as Servicio[],
    servicio: null as Servicio | null,
    cargando: false as boolean,
    error: null as string | null,
  }),

  actions: {
    async obtenerServicios() {
      try {
        this.cargando = true
        const res = await servicioServices.obtenerServicios()
        this.servicios = res.data
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async obtenerServicio(id: number) {
      try {
        this.cargando = true
        const res = await servicioServices.obtenerServicio(id)
        this.servicio = res.data
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async crearServicio(data: Servicio) {
      try {
        this.cargando = true
        const res = await servicioServices.crearServicio(data)
        this.servicios.push(res.data)
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async modificarServicio(id: number, data: Servicio) {
      try {
        this.cargando = true
        const res = await servicioServices.modificarServicio(id, data)

        const index = this.servicios.findIndex((s) => s.id === id)
        if (index !== -1) this.servicios[index] = res.data
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async eliminarServicio(id: number) {
      try {
        this.cargando = true
        await servicioServices.eliminarServicio(id)
        this.servicios = this.servicios.filter((s) => s.id !== id)
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },
  },
})
