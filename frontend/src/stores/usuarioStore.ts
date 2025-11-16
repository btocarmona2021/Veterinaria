// stores/usuarioStore.ts
import { defineStore } from 'pinia'
import usuarioServices from '@/services/usuarioServices'
import type { Usuario } from '@/Interfaces/usuarioInterface'

export const useUsuarioStore = defineStore('usuarioStore', {
  state: () => ({
    usuarios: [] as Usuario[],
    usuario: null as Usuario | null,
    cargando: false as boolean,
    error: null as string | null,
  }),

  actions: {
    async obtenerUsuarios() {
      this.cargando = true
      this.error = null

      try {
        const { data } = await usuarioServices.obtenerUsuarios()
        this.usuarios = data
      } catch (err: any) {
        this.error = err.message || 'Error al obtener usuarios'
      } finally {
        this.cargando = false
      }
    },

    async obtenerUsuario(id: number) {
      this.cargando = true
      this.error = null

      try {
        const { data } = await usuarioServices.obtenerUsuario(id)
        this.usuario = data
      } catch (err: any) {
        this.error = err.message || 'Error al obtener usuario'
      } finally {
        this.cargando = false
      }
    },

    async crearUsuario(usuario: Usuario) {
      this.cargando = true
      this.error = null

      try {
        const { data } = await usuarioServices.crearUsuario(usuario)
        this.usuarios.push(data)
        return data
      } catch (err: any) {
        this.error = err.message || 'Error al crear usuario'
      } finally {
        this.cargando = false
      }
    },

    async modificarUsuario(id: number, usuario: Usuario) {
      this.cargando = true
      this.error = null

      try {
        const { data } = await usuarioServices.modificarUsuario(id, usuario)

        // Reemplaza en el array
        this.usuarios = this.usuarios.map((u) => (u.id === id ? data : u))

        if (this.usuario?.id === id) {
          this.usuario = data
        }

        return data
      } catch (err: any) {
        this.error = err.message || 'Error al actualizar usuario'
      } finally {
        this.cargando = false
      }
    },

    async eliminarUsuario(id: number) {
      this.cargando = true
      this.error = null

      try {
        await usuarioServices.eliminarUsuario(id)

        this.usuarios = this.usuarios.filter((u) => u.id !== id)

        if (this.usuario?.id === id) {
          this.usuario = null
        }
        return true
      } catch (err: any) {
        this.error = err.message || 'Error al eliminar usuario'
      } finally {
        this.cargando = false
      }
    },
  },
})
