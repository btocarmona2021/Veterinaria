import { defineStore } from 'pinia'
import { ref } from 'vue'
import mascotaServices from '@/services/mascotaServices'
import type { Mascota } from '@/Interfaces/mascotaInterface'

export const useMascotaStore = defineStore('mascotaStore', () => {
  const mascotas = ref<Mascota[]>([])
  const mascota = ref<Mascota | null>(null)
  const cargando = ref(false)
  const error = ref<string | null>(null)

  const obtenerMascotas = async () => {
    cargando.value = true
    try {
      const res = await mascotaServices.obtenerMascotas()
      mascotas.value = res.data
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const obtenerMascotasFront = async () => {
    cargando.value = true
    try {
      const res = await mascotaServices.obtenerMascotasFront()
      mascotas.value = res.data
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const obtenerMascota = async (id: number) => {
    cargando.value = true
    try {
      const res = await mascotaServices.obtenerMascota(id)
      mascota.value = res.data
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const crearMascota = async (data: Mascota) => {
    cargando.value = true
    try {
      const res = await mascotaServices.crearMascota(data)
      mascotas.value.push(res.data)
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const modificarMascota = async (id: number, data: Mascota) => {
    cargando.value = true
    try {
      const res = await mascotaServices.modificarMascota(id, data)
      const index = mascotas.value.findIndex((m) => m.id === id)
      if (index !== -1) mascotas.value[index] = res.data
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  const eliminarMascota = async (id: number) => {
    cargando.value = true
    try {
      await mascotaServices.eliminarMascota(id)
      mascotas.value = mascotas.value.filter((m) => m.id !== id)
      return true
    } catch (err: any) {
      error.value = err.message
      throw err
    } finally {
      cargando.value = false
    }
  }

  return {
    mascotas,
    mascota,
    cargando,
    error,
    obtenerMascotas,
    obtenerMascotasFront,
    obtenerMascota,
    crearMascota,
    modificarMascota,
    eliminarMascota,
  }
})
