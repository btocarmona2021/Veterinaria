import { defineStore } from 'pinia'
import { ref } from 'vue'
import turnoServices from '@/services/turnoServices'
import type { Turno } from '@/Interfaces/turnoInterface'

export const useTurnoStore = defineStore('turnoStore', () => {
  const turnos = ref<Turno[]>([])
  const turno = ref<Turno | null>(null)
  const cargando = ref(false)
  const error = ref<string | null>(null)

  const obtenerTurnos = async () => {
    cargando.value = true
    try {
      const res = await turnoServices.obtenerTurnos()
      turnos.value = res.data
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const obtenerTurno = async (id: number) => {
    cargando.value = true
    try {
      const res = await turnoServices.obtenerTurno(id)
      turno.value = res.data
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const crearTurno = async (data: Turno) => {
    cargando.value = true
    try {
      const res = await turnoServices.crearTurno(data)
      turnos.value.push(res.data)
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const modificarTurno = async (id: number, data: Turno) => {
    cargando.value = true
    try {
      const res = await turnoServices.modificarTurno(id, data)
      const index = turnos.value.findIndex((t) => t.id === id)
      if (index !== -1) turnos.value[index] = res.data
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const eliminarTurno = async (id: number) => {
    cargando.value = true
    try {
      await turnoServices.eliminarTurno(id)
      turnos.value = turnos.value.filter((t) => t.id !== id)
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  return {
    turnos,
    turno,
    cargando,
    error,
    obtenerTurnos,
    obtenerTurno,
    crearTurno,
    modificarTurno,
    eliminarTurno,
  }
})
