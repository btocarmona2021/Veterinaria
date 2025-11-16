export interface Mascota {
  id: number
  nombre: string
  especie: string
  raza?: string
  edad?: number
  fecha_nacimiento?: string
  sexo?: 'Macho' | 'Hembra'
  color?: string
  peso?: number
  id_usuario: number
  fecha_registro?: string

  usuario_nombre?: string
  usuario_apellido?: string
}
