<script setup lang="ts">
import { ref, onMounted } from 'vue'

// 📌 STORES
import { useTurnoStore } from '@/stores/turnoStore'
import { useMascotaStore } from '@/stores/mascotaStore'
import { useUsuarioStore } from '@/stores/usuarioStore'
import { useServicioStore } from '@/stores/servicioStore'

import type { Turno } from '@/Interfaces/turnoInterface'

// 📌 Instancias de stores
const turnoStore = useTurnoStore()
const mascotaStore = useMascotaStore()
const usuarioStore = useUsuarioStore()
const servicioStore = useServicioStore()

// 📌 Campos del formulario
const mascotaId = ref<number | null>(null)
const veterinarioId = ref<number | null>(null)
const servicioId = ref<number | null>(null)
const fecha = ref('')
const hora = ref('')
const motivo = ref('')

const error = ref('')

onMounted(() => {
  mascotaStore.obtenerMascotas()
  usuarioStore.obtenerUsuarios()    // veterinarios salen de usuarios
  servicioStore.obtenerServicios()  // cargar lista de servicios
})

// 📌 Crear turno
const crearTurno = async () => {
  if (!mascotaId.value || !veterinarioId.value || !servicioId.value || !fecha.value || !hora.value) {
    error.value = 'Todos los campos son obligatorios.'
    return
  }


  const nuevoTurno = {
    id:0,
    estado: 'pendiente',
    fecha_creacion:fecha.value,
    fecha_hora: hora.value,
    id_mascota: mascotaId.value,
    notas: motivo.value,
    id_veterinario: veterinarioId.value,
    id_servicio: servicioId.value,
  }

  try {
    await turnoStore.crearTurno(nuevoTurno)

    mascotaId.value = null
    veterinarioId.value = null
    servicioId.value = null
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

      <!-- SELECT MASCOTA -->
      <div class="mb-3">
        <label class="form-label">Mascota</label>
        <select v-model="mascotaId" class="form-select">
          <option value="">Seleccione una mascota</option>
          <option
            v-for="m in mascotaStore.mascotas"
            :key="m.id"
            :value="m.id"
          >
            {{ m.nombre }} — (Dueño: {{ m.duenio_id }})
          </option>
        </select>
      </div>

      <!-- SELECT VETERINARIO -->
      <div class="mb-3">
        <label class="form-label">Veterinario</label>
        <select v-model="veterinarioId" class="form-select">
          <option value="">Seleccione un veterinario</option>

          <option
            v-for="v in usuarioStore.usuarios.filter(u => u.rol === 'veterinario')"
            :key="v.id"
            :value="v.id"
          >
            {{ v.nombre }} {{ v.apellido }}
          </option>
        </select>
      </div>

      <!-- SELECT SERVICIO -->
      <div class="mb-3">
        <label class="form-label">Servicio</label>
        <select v-model="servicioId" class="form-select">
          <option value="">Seleccione un servicio</option>

          <option
            v-for="s in servicioStore.servicios"
            :key="s.id"
            :value="s.id"
          >
            {{ s.nombre }} — ${{ s.precio }} ({{ s.duracion_estimada }} min)
          </option>
        </select>
      </div>

      <!-- FECHA -->
      <div class="mb-3">
        <label class="form-label">Fecha</label>
        <input v-model="fecha" type="date" class="form-control" />
      </div>

      <!-- HORA -->
      <div class="mb-3">
        <label class="form-label">Hora</label>
        <input v-model="hora" type="time" class="form-control" />
      </div>

      <!-- MOTIVO -->
      <div class="mb-3">
        <label class="form-label">Motivo</label>
        <input v-model="motivo" type="text" class="form-control" placeholder="Motivo del turno..." />
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
