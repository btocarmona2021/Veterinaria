<script setup lang="ts">
import { ref } from 'vue'
import { useHistorialStore } from '@/stores/historialStore'
import type { HistorialClinico } from '@/Interfaces/historialInterface'

const historialStore = useHistorialStore()

const mascotaId = ref<number | null>(null)
const veterinarioId = ref<number | null>(null)
const diagnostico = ref('')
const tratamiento = ref('')
const notas = ref('')

const error = ref('')

const crearHistorial = async () => {
  if (!mascotaId.value || !veterinarioId.value || !diagnostico.value) {
    error.value = 'Mascota, veterinario y diagnóstico son obligatorios.'
    return
  }

  const nuevoHistorial: HistorialClinico = {
    id: 0,
    mascota_id: mascotaId.value,
    veterinario_id: veterinarioId.value,
    fecha: new Date().toISOString(),
    diagnostico: diagnostico.value,
    tratamiento: tratamiento.value,
    notas: notas.value
  }

  try {
    await historialStore.crearHistorial(nuevoHistorial)

    mascotaId.value = null
    veterinarioId.value = null
    diagnostico.value = ''
    tratamiento.value = ''
    notas.value = ''
    error.value = ''

    alert('Historial creado correctamente')

  } catch (err) {
    console.error(err)
    error.value = 'Error al crear historial.'
  }
}
</script>

<template>
  <div class="container mt-4">
    <h2>Crear Historial Clínico</h2>

    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <form @submit.prevent="crearHistorial">
      <div class="mb-3">
        <label class="form-label">ID Mascota</label>
        <input v-model="mascotaId" type="number" class="form-control" />
      </div>

      <div class="mb-3">
        <label class="form-label">ID Veterinario</label>
        <input v-model="veterinarioId" type="number" class="form-control" />
      </div>

      <div class="mb-3">
        <label class="form-label">Diagnóstico</label>
        <textarea v-model="diagnostico" class="form-control"></textarea>
      </div>

      <div class="mb-3">
        <label class="form-label">Tratamiento</label>
        <textarea v-model="tratamiento" class="form-control"></textarea>
      </div>

      <div class="mb-3">
        <label class="form-label">Notas</label>
        <textarea v-model="notas" class="form-control"></textarea>
      </div>

      <button class="btn btn-primary">Crear Historial</button>
    </form>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
}
</style>
