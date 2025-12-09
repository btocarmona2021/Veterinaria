export interface Usuario {
  id: number
  nombre: string
  apellido: string
  email: string
  telefono: string
  direccion: string
  rol: 'administrador' | 'veterinario' | 'cliente'
  especialidad:
    | 'Clínico General'
    | 'Cirujano'
    | 'Anestesista'
    | 'Dermatologo'
    | 'Oftalmologo'
    | null
  disponible: boolean
  fecha_registro: string
  activo: boolean
  password: string
}
