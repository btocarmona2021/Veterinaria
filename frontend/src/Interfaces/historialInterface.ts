export interface Historial {
  id: number
  id_mascota: number
  fecha: string
  id_veterinario?: number
  diagnostico?: string
  tratamiento?: string
  observaciones?: string
  peso_actual?: number
  proxima_visita?: string

  mascota_nombre?: string
  especie?: string
  raza?: string

  veterinario_nombre?: string
  veterinario_apellido?: string
  especialidad?: string
}
