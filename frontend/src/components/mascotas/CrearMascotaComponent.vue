<!-- components/mascotas/CrearMascotaComponent.vue -->
<script setup lang="ts">
import { ref } from 'vue'
import { useMascotaStore } from '@/stores/mascotaStore'
import type { Mascota } from '@/Interfaces/mascotaInterface'

const mascotaStore = useMascotaStore()

// Campos del formulario
const nombre = ref('')
const especie = ref('')
const raza = ref('')
const edad = ref<number | null>(null)
const fecha_nacimiento = ref('')
const sexo = ref<'Macho' | 'Hembra'>('Macho')
const color = ref('')
const peso = ref<number|null>(null)
const id_usuario = ref<number | null>(null) // dueño

const error = ref('')

const crearMascota = async () => {
  if (!nombre.value || !especie.value || !id_usuario.value) {
    error.value = 'Nombre, especie y dueño son obligatorios.'
    return
  }

  const nuevaMascota: Mascota = {
    id: 0,
    nombre: nombre.value,
    especie: especie.value,
    raza: raza.value,
    edad: edad.value || 0,
    fecha_nacimiento: fecha_nacimiento.value,
    sexo: sexo.value,
    color: color.value,
    peso: peso.value || 0 ,
    id_usuario: id_usuario.value,
    fecha_registro: '',
  }

  try {
    await mascotaStore.crearMascota(nuevaMascota)
    // Limpiar campos
    nombre.value = ''
    especie.value = ''
    raza.value = ''
    edad.value = null
    fecha_nacimiento.value = ''
    sexo.value = 'Macho'
    color.value = ''
    peso.value = null
    id_usuario.value = null
    error.value = ''
    alert('Mascota creada correctamente')
  } catch (err) {
    console.error(err)
    error.value = 'Error al crear la mascota.'
  }
}
</script>

<template>
  <div class="container mt-4">
    <h2>Crear Mascota</h2>
    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <form @submit.prevent="crearMascota">
      <div class="mb-3">
        <label class="form-label">Nombre</label>
        <input v-model="nombre" type="text" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Especie</label>
        <input v-model="especie" type="text" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Raza</label>
        <input v-model="raza" type="text" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Edad</label>
        <input v-model="edad" type="number" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Fecha de Nacimiento</label>
        <input v-model="fecha_nacimiento" type="date" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Sexo</label>
        <select v-model="sexo" class="form-select">
          <option value="Macho">Macho</option>
          <option value="Hembra">Hembra</option>
        </select>
      </div>
      <div class="mb-3">
        <label class="form-label">Color</label>
        <input v-model="color" type="text" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Peso</label>
        <input v-model="peso" type="number" step="0.1" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Dueño (ID Usuario)</label>
        <input v-model="id_usuario" type="number" class="form-control" />
      </div>
      <button type="submit" class="btn btn-primary">Crear Mascota</button>
    </form>
  </div>
</template>
