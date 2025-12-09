import type { Usuario } from "./usuarioInterface"
export interface Mascota {
  color: string
  duenio?: Usuario
  edad: number
  especie: string
  fecha_nacimiento: string
  fecha_registro: string
  id: number
  id_usuario: number
  nombre: string
  peso: number
  raza: string
  sexo: 'Macho' | 'Hembra'
}

