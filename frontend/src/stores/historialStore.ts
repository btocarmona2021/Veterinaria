import { defineStore } from 'pinia'
import { ref } from 'vue'
import historialServices from '@/services/historialServices'
import type { Historial } from '@/Interfaces/historialInterface'

export const useHistorialStore = defineStore('historialStore', () => {
  const historiales = ref<Historial[]>([])
  const historial = ref<Historial | null>(null)
  const cargando = ref(false)
  const error = ref<string | null>(null)

  const obtenerHistoriales = async () => {
    cargando.value = true
    try {
      const res = await historialServices.obtenerHistoriales()
      historiales.value = res.data
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const obtenerHistorial = async (id: number) => {
    cargando.value = true
    try {
      const res = await historialServices.obtenerHistorial(id)
      historial.value = res.data
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const crearHistorial = async (h: Historial) => {
    cargando.value = true
    try {
      const res = await historialServices.crearHistorial(h)
      historiales.value.push(res.data)
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const modificarHistorial = async (id: number, h: Historial) => {
    cargando.value = true
    try {
      const res = await historialServices.modificarHistorial(id, h)
      const index = historiales.value.findIndex((i) => Number(i.id) === id)
      if (index !== -1) historiales.value[index] = res.data
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const eliminarHistorial = async (id: number) => {
    cargando.value = true
    try {
      await historialServices.eliminarHistorial(id)
      historiales.value = historiales.value.filter((h) => Number(h.id) !== id)
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  return {
    historiales,
    historial,
    cargando,
    error,
    obtenerHistoriales,
    obtenerHistorial,
    crearHistorial,
    modificarHistorial,
    eliminarHistorial,
  }
})
