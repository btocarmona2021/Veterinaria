export interface Turno {
  estado:         string;
  fecha_creacion: string;
  fecha_hora:     string;
  id:             number;
  mascota?:        Mascota;
  notas:          string;
  servicio?:       Servicio;
  veterinario?:    Veterinario;
}

export interface Mascota {
  id:     number;
  nombre: string;
  raza:   string;
}

export interface Servicio {
  id:     number;
  nombre: string;
  precio: string;
}

export interface Veterinario {
  apellido: string;
  id:       number;
  nombre:   string;
}
