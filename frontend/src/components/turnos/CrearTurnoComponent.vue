<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Icon } from '@iconify/vue'
import Swal from 'sweetalert2'

import { useTurnoStore } from '@/stores/turnoStore'
import { useMascotaStore } from '@/stores/mascotaStore'
import { useUsuarioStore } from '@/stores/usuarioStore'
import { useServicioStore } from '@/stores/servicioStore'
import useAuthStore from '@/stores/authStore'
import type { Turno } from '@/Interfaces/turnoInterface'

const turnoStore = useTurnoStore()
const mascotaStore = useMascotaStore()
const usuarioStore = useUsuarioStore()
const servicioStore = useServicioStore()
const authStore = useAuthStore()

const idMascota = ref<number | null>(null)
const idVeterniario = ref<number | null>(null)
const idServicio = ref<number | null>(null)
const fecha_creacion = ref('')
const fecha_hora = ref('')
const notas = ref('')
const error = ref('')

onMounted(() => {
  mascotaStore.obtenerMascotas()
  usuarioStore.obtenerUsuarios()
  servicioStore.obtenerServicios()
})

const crearTurno = async () => {
  if (
    !idMascota.value ||
    !idVeterniario.value ||
    !idServicio.value ||
    !fecha_creacion.value ||
    !fecha_hora.value
  ) {
    error.value = 'Todos los campos son obligatorios.'
    return
  }

  const nuevoTurno: Turno = {
    id: 0,
    estado: 'pendiente',
    fecha_creacion: fecha_creacion.value,
    fecha_hora: fecha_hora.value,
    id_mascota: idMascota.value,
    id_servicio: idServicio.value,
    id_veterinario: idVeterniario.value,
    notas: notas.value,
  }

  try {
    await turnoStore.crearTurno(nuevoTurno)

    idMascota.value = null
    idVeterniario.value = null
    idServicio.value = null
    fecha_creacion.value = ''
    fecha_hora.value = ''
    notas.value = ''
    error.value = ''

    Swal.fire({
      title: '¡Turno creado!',
      text: 'El turno se registró correctamente.',
      icon: 'success',
      confirmButtonColor: '#6366f1',
    })
  } catch (err:any) {
    error.value = 'Error al crear turno.'

    Swal.fire({
      title: 'Error',
      text: 'No se pudo crear el turno.',
      icon: 'error',
      confirmButtonColor: '#6366f1',
    })
  }
}
</script>

<template>
  <div class="page">
    <div class="card">
      <h2 class="title">
        <Icon icon="mdi:calendar-plus" class="icon" />
        Crear Turno
      </h2>

      <div v-if="error" class="error-msg"><Icon icon="mdi:alert-circle" /> {{ error }}</div>

      <form @submit.prevent="crearTurno">
        <div class="input-group">
          <label>Mascota</label>
          <div class="input-box">
            <Icon icon="mdi:paw" class="input-icon" />
            <select v-if="authStore.usuarioAutorizado.rol === 'cliente'" v-model="idMascota">
              <option
                v-for="m in mascotaStore.mascotas.filter(
                  (ms) => ms.id_usuario === authStore.usuarioAutorizado.id,
                )"
                :key="m.id"
                :value="m.id"
              >
                {{ m.nombre }}
              </option>
            </select>
            <select v-if="authStore.usuarioAutorizado.rol === 'administrador'" v-model="idMascota">
              <option v-for="m in mascotaStore.mascotas" :key="m.id" :value="m.id">
                {{ m.nombre }}
              </option>
            </select>
          </div>
        </div>

        <div class="input-group">
          <label>Veterinario</label>
          <div class="input-box">
            <Icon icon="mdi:stethoscope" class="input-icon" />
            <select v-model="idVeterniario">
              <option value="">Seleccione un veterinario</option>
              <option
                v-for="v in usuarioStore.usuarios.filter((u) => u.rol === 'veterinario')"
                :key="v.id"
                :value="v.id"
              >
                {{ v.nombre }} {{ v.apellido }}
              </option>
            </select>
          </div>
        </div>

        <div class="input-group">
          <label>Servicio</label>
          <div class="input-box">
            <Icon icon="mdi:needle" class="input-icon" />
            <select v-model="idServicio">
              <option value="">Seleccione un servicio</option>
              <option v-for="s in servicioStore.servicios" :key="s.id" :value="s.id">
                {{ s.nombre }} — ${{ s.precio }} ({{ s.duracion_estimada }} min)
              </option>
            </select>
          </div>
        </div>

        <div class="input-group">
          <label>Fecha</label>
          <div class="input-box">
            <Icon icon="mdi:calendar" class="input-icon" />
            <input type="date" v-model="fecha_creacion" />
          </div>
        </div>

        <div class="input-group">
          <label>Hora</label>
          <div class="input-box">
            <Icon icon="mdi:clock-outline" class="input-icon" />
            <input type="time" v-model="fecha_hora" />
          </div>
        </div>

        <div class="input-group">
          <label>Motivo</label>
          <div class="input-box">
            <Icon icon="mdi:note-edit" class="input-icon" />
            <input type="text" v-model="notas" placeholder="Motivo del turno..." />
          </div>
        </div>

        <button class="btn-submit">
          <Icon icon="mdi:check-bold" class="btn-icon" />
          Crear Turno
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
  max-width: 500px;
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
  margin-bottom: 2px;
  margin-right: 10px;
  display: block;
}

.input-box {
  position: relative;
}

.input-box select,
.input-box input {
  width: 100%;
  padding: 12px 12px 12px 42px;
  border-radius: 10px;
  border: 1px solid #ccc;
  transition: 0.2s ease;
  background: #fafafa;
}

.input-box select:focus,
.input-box input:focus {
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
