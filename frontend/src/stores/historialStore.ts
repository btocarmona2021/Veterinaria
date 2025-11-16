// stores/historialStore.ts
import { defineStore } from 'pinia'
import historialServices from '@/services/historialServices'
import type { Historial } from '@/Interfaces/historialInterface'

export const useHistorialStore = defineStore('historialStore', {
  state: () => ({
    historiales: [] as Historial[],
    historial: null as Historial | null,
    cargando: false as boolean,
    error: null as string | null,
  }),

  actions: {
    async obtenerHistoriales() {
      try {
        this.cargando = true
        const res = await historialServices.obtenerHistoriales()
        this.historiales = res.data
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async obtenerHistorial(id: number) {
      try {
        this.cargando = true
        const res = await historialServices.obtenerHistorial(id)
        this.historial = res.data
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async crearHistorial(historial: Historial) {
      try {
        this.cargando = true
        const res = await historialServices.crearHistorial(historial)
        this.historiales.push(res.data)
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async modificarHistorial(id: number, historial: Historial) {
      try {
        this.cargando = true
        const res = await historialServices.modificarHistorial(id, historial)

        const index = this.historiales.findIndex((h) => h.id === id)
        if (index !== -1) {
          this.historiales[index] = res.data
        }
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async eliminarHistorial(id: number) {
      try {
        this.cargando = true
        await historialServices.eliminarHistorial(id)

        this.historiales = this.historiales.filter((h) => h.id !== id)
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },
  },
})
