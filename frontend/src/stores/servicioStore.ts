import { defineStore } from 'pinia'
import { ref } from 'vue'
import servicioServices from '@/services/servicioServices'
import type { Servicio } from '@/Interfaces/servicioInterface'

export const useServicioStore = defineStore('servicioStore', () => {
  const servicios = ref<Servicio[]>([])
  const servicio = ref<Servicio | null>(null)
  const cargando = ref(false)
  const error = ref<string | null>(null)

  const obtenerServicios = async () => {
    cargando.value = true
    try {
      const res = await servicioServices.obtenerServicios()
      servicios.value = res.data
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const obtenerServicio = async (id: number) => {
    cargando.value = true
    try {
      const res = await servicioServices.obtenerServicio(id)
      servicio.value = res.data
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const crearServicio = async (data: Servicio) => {
    cargando.value = true
    try {
      const res = await servicioServices.crearServicio(data)
      if (res?.data) servicios.value.push(res.data)
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const modificarServicio = async (id: number, data: Servicio) => {
    cargando.value = true
    try {
      const res = await servicioServices.modificarServicio(id, data)
      const index = servicios.value.findIndex((s) => s.id === id)
      if (index !== -1) servicios.value[index] = res.data
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const eliminarServicio = async (id: number) => {
    cargando.value = true
    try {
      await servicioServices.eliminarServicio(id)
      servicios.value = servicios.value.filter((s) => s.id !== id)
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  return {
    servicios,
    servicio,
    cargando,
    error,
    obtenerServicios,
    obtenerServicio,
    crearServicio,
    modificarServicio,
    eliminarServicio,
  }
})
