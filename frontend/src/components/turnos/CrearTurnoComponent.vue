<script setup lang="ts">
import { ref } from 'vue'
import { useTurnoStore } from '@/stores/turnoStore'
import type { Turno } from '@/Interfaces/turnoInterface'

const turnoStore = useTurnoStore()

const mascotaId = ref<number | null>(null)
const veterinarioId = ref<number | null>(null)
const fecha = ref('')
const hora = ref('')
const motivo = ref('')

const error = ref('')

const crearTurno = async () => {
  if (!mascotaId.value || !veterinarioId.value || !fecha.value || !hora.value) {
    error.value = 'Todos los campos son obligatorios.'
    return
  }

  const nuevoTurno: Turno = {
    id: 0,
    mascota_id: mascotaId.value,
    veterinario_id: veterinarioId.value,
    fecha: fecha.value,
    hora: hora.value,
    motivo: motivo.value,
    estado: 'pendiente'
  }

  try {
    await turnoStore.crearTurno(nuevoTurno)

    mascotaId.value = null
    veterinarioId.value = null
    fecha.value = ''
    hora.value = ''
    motivo.value = ''
    error.value = ''

    alert('Turno creado correctamente')

  } catch (err) {
    console.error(err)
    error.value = 'Error al crear turno.'
  }
}
</script>

<template>
  <div class="container mt-4">
    <h2>Crear Turno</h2>

    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <form @submit.prevent="crearTurno">
      <div class="mb-3">
        <label class="form-label">ID Mascota</label>
        <input v-model="mascotaId" type="number" class="form-control" />
      </div>

      <div class="mb-3">
        <label class="form-label">ID Veterinario</label>
        <input v-model="veterinarioId" type="number" class="form-control" />
      </div>

      <div class="mb-3">
        <label class="form-label">Fecha</label>
        <input v-model="fecha" type="date" class="form-control" />
      </div>

      <div class="mb-3">
        <label class="form-label">Hora</label>
        <input v-model="hora" type="time" class="form-control" />
      </div>

      <div class="mb-3">
        <label class="form-label">Motivo</label>
        <input v-model="motivo" type="text" class="form-control" />
      </div>

      <button class="btn btn-primary">Crear Turno</button>
    </form>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
}
</style>
