export interface Usuario {
  id: number
  nombre: string
  apellido?: string
  email: string
  telefono?: string
  direccion?: string
  rol: 'administrador' | 'veterinario' | 'cliente'
  especialidad?: string
  disponible?: number
  fecha_registro?: string
  activo: number
}
