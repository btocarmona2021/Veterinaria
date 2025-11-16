// stores/turnoStore.ts
import { defineStore } from 'pinia'
import turnoServices from '@/services/turnoServices'
import type { Turno } from '@/Interfaces/turnoInterface'

export const useTurnoStore = defineStore('turnoStore', {
  state: () => ({
    turnos: [] as Turno[],
    turno: null as Turno | null,
    cargando: false as boolean,
    error: null as string | null,
  }),

  actions: {
    async obtenerTurnos() {
      try {
        this.cargando = true
        const res = await turnoServices.obtenerTurnos()
        this.turnos = res.data
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async obtenerTurno(id: number) {
      try {
        this.cargando = true
        const res = await turnoServices.obtenerTurno(id)
        this.turno = res.data
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async crearTurno(data: Turno) {
      try {
        this.cargando = true
        const res = await turnoServices.crearTurno(data)
        this.turnos.push(res.data)
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async modificarTurno(id: number, data: Turno) {
      try {
        this.cargando = true
        const res = await turnoServices.modificarTurno(id, data)

        const index = this.turnos.findIndex((t) => t.id === id)
        if (index !== -1) this.turnos[index] = res.data
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },

    async eliminarTurno(id: number) {
      try {
        this.cargando = true
        await turnoServices.eliminarTurno(id)

        this.turnos = this.turnos.filter((t) => t.id !== id)
      } catch (err: any) {
        this.error = err.message
      } finally {
        this.cargando = false
      }
    },
  },
})
