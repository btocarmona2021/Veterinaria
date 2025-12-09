export interface AuthUser {
  id: number
  nombre_apellido?:string,
  email: string
  password?:string
  jwt: string
  rol: string
  message:string
}
