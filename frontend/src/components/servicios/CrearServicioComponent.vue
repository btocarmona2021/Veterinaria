<script setup lang="ts">
import { ref } from 'vue'
import { useServicioStore } from '@/stores/servicioStore'
import type { Servicio } from '@/Interfaces/servicioInterface'

const servicioStore = useServicioStore()
const nombre = ref('')
const descripcion = ref('')
const precio = ref<number | null>(null)
const duracion_estimada = ref<number | null>(null)
const error = ref('')

const crearServicio = async () => {
  if (!nombre.value || precio.value === null || duracion_estimada.value === null) {
    error.value = 'Nombre, precio y duración son obligatorios.'
    return
  }

  const nuevoServicio: Servicio = {
    id: 0,
    nombre: nombre.value,
    descripcion: descripcion.value,
    precio: precio.value,
    duracion_estimada: duracion_estimada.value,
  }

  try {
    await servicioStore.crearServicio(nuevoServicio)
    nombre.value = ''
    descripcion.value = ''
    precio.value = null
    duracion_estimada.value = null
    error.value = ''
    alert('Servicio creado correctamente')
  } catch (err) {
    console.error(err)
    error.value = 'Error al crear el servicio.'
  }
}
</script>

<template>
  <div class="container mt-4">
    <h2>Crear Servicio</h2>
    <div v-if="error" class="alert alert-danger">{{ error }}</div>
    <form @submit.prevent="crearServicio">
      <div class="mb-3">
        <label class="form-label">Nombre</label>
        <input v-model="nombre" type="text" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Descripción</label>
        <textarea v-model="descripcion" class="form-control"></textarea>
      </div>
      <div class="mb-3">
        <label class="form-label">Precio</label>
        <input v-model="precio" type="number" step="0.01" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Duración estimada (minutos)</label>
        <input v-model="duracion_estimada" type="number" class="form-control" />
      </div>
      <button type="submit" class="btn btn-primary">Crear Servicio</button>
    </form>
  </div>
</template>
