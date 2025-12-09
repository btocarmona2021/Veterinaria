import { defineStore } from 'pinia'
import { ref } from 'vue'
import usuarioServices from '@/services/usuarioServices'
import type { Usuario } from '@/Interfaces/usuarioInterface'

export const useUsuarioStore = defineStore('usuarioStore', () => {
  const usuarios = ref<Usuario[]>([])
  const usuario = ref<Usuario | null>(null)
  const cargando = ref(false)
  const error = ref<string | null>(null)

  const obtenerUsuarios = async () => {
    cargando.value = true
    error.value = null
    try {
      const { data } = await usuarioServices.obtenerUsuarios()
      usuarios.value = data
    } catch (err: any) {
      error.value = err.message || 'Error al obtener usuarios'
      throw err
    } finally {
      cargando.value = false
    }
  }

  const obtenerUsuario = async (id: number) => {
    cargando.value = true
    error.value = null
    try {
      const { data } = await usuarioServices.obtenerUsuario(id)
      usuario.value = data
    } catch (err: any) {
      error.value = err.message || 'Error al obtener usuario'
      throw err
    } finally {
      cargando.value = false
    }
  }

  const crearUsuario = async (nuevoUsuario: Usuario) => {
    cargando.value = true
    error.value = null
    try {
      const { data } = await usuarioServices.crearUsuario(nuevoUsuario)
      usuarios.value.push(data)
      return data
    } catch (err: any) {
      error.value = err.message || 'Error al crear usuario'
      throw err
    } finally {
      cargando.value = false
    }
  }

  const modificarUsuario = async (id: number, datos: Usuario) => {
    cargando.value = true
    error.value = null
    try {
      const { data } = await usuarioServices.modificarUsuario(id, datos)
      usuarios.value = usuarios.value.map((u) => (u.id === id ? data : u))
      if (usuario.value?.id === id) usuario.value = data
      return data
    } catch (err: any) {
      error.value = err.message || 'Error al actualizar usuario'
      throw err
    } finally {
      cargando.value = false
    }
  }

  const eliminarUsuario = async (id: number) => {
    cargando.value = true
    error.value = null
    try {
      await usuarioServices.eliminarUsuario(id)
      usuarios.value = usuarios.value.filter((u) => u.id !== id)
      if (usuario.value?.id === id) usuario.value = null
      return true
    } catch (err: any) {
      error.value = err.message || 'Error al eliminar usuario'
    } finally {
      cargando.value = false
    }
  }

  return {
    usuarios,
    usuario,
    cargando,
    error,
    obtenerUsuarios,
    obtenerUsuario,
    crearUsuario,
    modificarUsuario,
    eliminarUsuario,
  }
})
