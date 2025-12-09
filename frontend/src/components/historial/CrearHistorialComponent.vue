<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useHistorialStore } from '@/stores/historialStore'
import { useMascotaStore } from '@/stores/mascotaStore'
import { useUsuarioStore } from '@/stores/usuarioStore'
import type { Historial } from '@/Interfaces/historialInterface'
import { useRouter } from 'vue-router'
import { Icon } from '@iconify/vue'
import Swal from 'sweetalert2'

const router = useRouter()
const historialStore = useHistorialStore()
const mascotaStore = useMascotaStore()
const usuarioStore = useUsuarioStore()

const mascotaId = ref<number | null>(null)
const veterinarioId = ref<number | null>(null)
const fecha = ref('')
const diagnostico = ref('')
const tratamiento = ref('')
const observaciones = ref('')
const pesoActual = ref('')
const proximaVisita = ref('')

const error = ref('')

const crearHistorial = async () => {
  if (!mascotaId.value || !veterinarioId.value || !diagnostico.value) {
    error.value = 'Mascota, veterinario y diagnóstico son obligatorios.'
    return
  }

  const nuevoHistorial: Historial = {
    id: '',
    id_mascota: mascotaId.value,
    id_veterinario: veterinarioId.value,
    fecha: fecha.value,
    diagnostico: diagnostico.value,
    tratamiento: tratamiento.value,
    peso_actual: pesoActual.value,
    proxima_visita: proximaVisita.value,
    observaciones: observaciones.value,
  }

  try {
    await historialStore.crearHistorial(nuevoHistorial)

    mascotaId.value = null
    veterinarioId.value = null
    fecha.value = ''
    diagnostico.value = ''
    tratamiento.value = ''
    pesoActual.value = ''
    proximaVisita.value = ''
    observaciones.value = ''
    error.value = ''
    await Swal.fire({
      title: '¡Historial creado!',
      text: 'El historial clínico se registró correctamente.',
      icon: 'success',
      confirmButtonColor: '#6366f1',
    })
    router.push({ name: 'listarHistorial' })
  } catch (err:any) {
    console.error(err)
    error.value = 'Error al crear el historial.'

    Swal.fire({
      title: 'Error',
      text: `${err.response?.data?.msg ==='Token has expired'? 'Debes iniciar sesion nuevamente su token ha expirado': err.response?.data?.msg}`,
      icon: 'error',
      confirmButtonColor: '#6366f1',
    })
  }
}

onMounted(async () => {
  await mascotaStore.obtenerMascotas()
  await usuarioStore.obtenerUsuarios()
}) 
</script>

<template>
  <div class="page">
    <div class="card">
      <h2 class="title">
        <Icon icon="mdi:clipboard-text" class="icon" /> Cargar Historial Clínico
      </h2>

      <div v-if="error" class="error-msg"><Icon icon="mdi:alert-circle" /> {{ error }}</div>

      <form @submit.prevent="crearHistorial">
        <div class="input-group">
          <label>Mascota</label>
          <div class="input-box">
            <select v-model="mascotaId">
              <option :value="null" disabled>Seleccione una mascota</option>
              <option
                v-for="mascota in mascotaStore.mascotas"
                :key="mascota.id"
                :value="mascota.id"
              >
                {{ mascota.nombre }}
              </option>
            </select>
            <Icon icon="mdi:dog" class="input-icon" />
          </div>
        </div>

        <div class="input-group">
          <label>Veterinario</label>
          <div class="input-box">
            <select v-model="veterinarioId">
              <option :value="null" disabled>Seleccione un veterinario</option>
              <option
                v-for="usuario in usuarioStore.usuarios.filter((u) => u.rol === 'veterinario')"
                :key="usuario.id"
                :value="usuario.id"
              >
                {{ usuario.nombre }} {{ usuario.apellido }}
              </option>
            </select>
            <Icon icon="mdi:account" class="input-icon" />
          </div>
        </div>

        <div class="input-group">
          <label>Fecha Consulta</label>
          <div class="input-box">
            <input type="date" v-model="fecha" />
            <Icon icon="mdi:calendar" class="input-icon" />
          </div>
        </div>

        <div class="input-group">
          <label>Diagnóstico</label>
          <div class="input-box">
            <textarea v-model="diagnostico" placeholder="Ingrese diagnóstico"></textarea>
            <Icon icon="mdi:clipboard-text" class="input-icon" />
          </div>
        </div>

        <div class="input-group">
          <label>Tratamiento</label>
          <div class="input-box">
            <textarea v-model="tratamiento" placeholder="Ingrese tratamiento"></textarea>
            <Icon icon="mdi:medication" class="input-icon" />
          </div>
        </div>

        <div class="input-group">
          <label>Peso Actual (kg)</label>
          <div class="input-box">
            <input type="number" step="0.1" v-model="pesoActual" placeholder="Peso actual" />
            <Icon icon="mdi:weight-kilogram" class="input-icon" />
          </div>
        </div>

        <div class="input-group">
          <label>Próxima Visita</label>
          <div class="input-box">
            <input type="date" v-model="proximaVisita" />
            <Icon icon="mdi:calendar-check" class="input-icon" />
          </div>
        </div>

        <div class="input-group">
          <label>Observaciones</label>
          <div class="input-box">
            <textarea v-model="observaciones" placeholder="Ingrese observaciones"></textarea>
            <Icon icon="mdi:note-text" class="input-icon" />
          </div>
        </div>

        <button type="submit" class="btn-submit">
          <Icon icon="mdi:plus-circle" class="btn-icon" /> Crear Historial
        </button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.page {
  width: 100%;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  padding: 20px;
  background-image: url('/img/fondo.png') !important;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

.card {
  width: 100%;
  max-width: 600px;
  background: white;
  padding: 35px;
  border-radius: 18px;
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.12);
}

.title {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 700;
  margin-bottom: 20px;
}

.icon {
  font-size: 28px;
}

.error-msg {
  background: #ffdddd;
  color: #b30000;
  border-left: 4px solid #b30000;
  padding: 10px;
  margin-bottom: 15px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.input-group {
  margin-bottom: 15px;
}

.input-group label {
  font-weight: 600;
  margin-bottom: 5px;
  display: block;
  margin-right: 10px;
}

.input-box {
  position: relative;
}

.input-box input,
.input-box select,
.input-box textarea {
  width: 100%;
  padding: 12px 12px 12px 42px;
  border-radius: 10px;
  border: 1px solid #ccc;
  transition: 0.2s ease;
  background: #fafafa;
  resize: vertical;
}

.input-box input:focus,
.input-box select:focus,
.input-box textarea:focus {
  border-color: #6366f1;
  background: white;
  outline: none;
}

.input-icon {
  position: absolute;
  top: 50%;
  left: 12px;
  transform: translateY(-50%);
  font-size: 20px;
  opacity: 0.7;
}

.btn-submit {
  width: 100%;
  display: flex;
  justify-content: center;
  gap: 8px;
  align-items: center;
  background: #6366f1;
  color: white;
  border: none;
  padding: 14px;
  border-radius: 10px;
  font-size: 16px;
  margin-top: 10px;
  cursor: pointer;
  transition: 0.2s;
}

.btn-submit:hover {
  background: #4f46e5;
}

.btn-icon {
  font-size: 20px;
}
</style>
