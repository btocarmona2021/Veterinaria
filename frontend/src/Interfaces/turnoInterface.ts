export interface Turno {
  id: number
  fecha_hora: string

  id_mascota: number
  id_veterinario?: number
  id_servicio?: number

  estado: 'pendiente' | 'confirmado' | 'completado' | 'cancelado'
  notas?: string
  fecha_creacion?: string


  mascota_nombre?: string
  mascota_especie?: string

  veterinario_nombre?: string
  veterinario_apellido?: string

  servicio_nombre?: string
}
