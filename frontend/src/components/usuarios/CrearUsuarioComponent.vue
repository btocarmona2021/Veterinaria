<script setup lang="ts">
import { ref } from 'vue'
import { useUsuarioStore } from '@/stores/usuarioStore'
import type { Usuario } from '@/Interfaces/usuarioInterface'

const usuarioStore = useUsuarioStore()

// Campos del formulario
const nombre = ref('')
const apellido = ref('')
const email = ref('')
const password = ref('')
const telefono = ref('')
const direccion = ref('')
const rol = ref<'administrador' | 'veterinario' | 'cliente'>('cliente')
const fecha_registro = ref('')
const especialidad = ref<'Cirujano'| 'Anestesista'>('Cirujano')

// Error de validación
const error = ref('')

// Función para enviar
const crearUsuario = async () => {
  if (!nombre.value || !email.value || !password.value) {
    error.value = 'Nombre, email y contraseña son obligatorios.'
    return
  }

  const nuevoUsuario: Usuario = {
    id: 0, // lo asigna el backend
    nombre: nombre.value,
    apellido: apellido.value,
    email: email.value,
    password: password.value,
    telefono: telefono.value,
    direccion: direccion.value,
    rol: rol.value,
    especialidad: especialidad.value,
    disponible: true,
    fecha_registro: fecha_registro.value,
    activo: true,
  }

  try {
    await usuarioStore.crearUsuario(nuevoUsuario)
    // Limpiar campos
    nombre.value = ''
    apellido.value = ''
    email.value = ''
    password.value = ''
    telefono.value = ''
    direccion.value = ''
    rol.value = 'cliente'
    error.value = ''
    alert('Usuario creado correctamente')
  } catch (err) {
    console.error(err)
    error.value = 'Error al crear usuario.'
  }
}
</script>

<template>
  <div class="container mt-4">
    <h2>Crear Usuario</h2>
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <form @submit.prevent="crearUsuario">
      <div class="mb-3">
        <label class="form-label">Nombre</label>
        <input v-model="nombre" type="text" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Apellido</label>
        <input v-model="apellido" type="text" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Email</label>
        <input v-model="email" type="email" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Contraseña</label>
        <input v-model="password" type="password" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Teléfono</label>
        <input v-model="telefono" type="text" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Dirección</label>
        <input v-model="direccion" type="text" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Rol</label>
        <select v-model="rol" class="form-select">
          <option value="administrador">Administrador</option>
          <option value="veterinario">Veterinario</option>
          <option value="cliente">Cliente</option>
        </select>
      </div>
      <div class="mb-3">
        <label class="form-label">Especialidad</label>
        <select v-model="especialidad" class="form-select">
          <option value="Cirujano">Cirujano</option>
          <option value="Anestesista">Anestesista</option>
        </select>
      </div>
        <div class="mb-3">
        <label class="form-label">Fecha de Registro</label>
        <input v-model="fecha_registro" type="date" class="form-control" />
      </div>
       <div class="mb-3">
        <label class="form-label px-4">Disponible</label>
        <input type="checkbox" checked="true" class="form-check-input " />
      </div>
      <button type="submit" class="btn btn-primary">Crear Usuario</button>
    </form>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
}
</style>
