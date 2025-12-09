import type { Mascota } from "./mascotaInterface";
import type { Servicio } from '@/Interfaces/servicioInterface';
import type{ Usuario } from "./usuarioInterface";

export interface Turno {
  id:             number;
  fecha_hora:     string;
  id_mascota:     number;
  id_veterinario: number;
  id_servicio:    number;
  estado:         string;
  notas:          string;
  fecha_creacion: string;
  mascota?:        Mascota
  servicio?:       Servicio
  veterinario?:    Usuario
}

