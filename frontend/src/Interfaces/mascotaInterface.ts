export interface Mascota {
  color:            string;
  duenio:           Duenio;
  edad:             number;
  especie:          string;
  fecha_nacimiento: string;
  fecha_registro:   string;
  id:               number;
  id_usuario:       number;
  nombre:           string;
  peso:             string;
  raza:             string;
  sexo:             string;
}

export interface Duenio {
  activo:         number;
  apellido:       string;
  direccion:      string;
  disponible:     number;
  email:          string;
  especialidad:   string;
  fecha_registro: string;
  id:             number;
  nombre:         string;
  rol:            string;
  telefono:       string;
}

