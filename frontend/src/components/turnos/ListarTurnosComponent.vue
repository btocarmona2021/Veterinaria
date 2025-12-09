<script setup lang="ts">
import { onMounted } from 'vue'
import { useTurnoStore } from '@/stores/turnoStore'
import { useUsuarioStore } from '@/stores/usuarioStore'
import { useMascotaStore } from '@/stores/mascotaStore'
import { useServicioStore } from '@/stores/servicioStore'
import type { Turno } from '@/Interfaces/turnoInterface'
import { useRouter } from 'vue-router'
import { Icon } from '@iconify/vue'
import Swal from 'sweetalert2'

const turnoStore = useTurnoStore()
const usuarioStore = useUsuarioStore()
const mascotaStore = useMascotaStore()
const servicioStore = useServicioStore()
const router = useRouter()

onMounted(async () => {
  await turnoStore.obtenerTurnos()
  await usuarioStore.obtenerUsuarios()
  await mascotaStore.obtenerMascotas()
  await servicioStore.obtenerServicios()
})

async function abrirModalEliminar(turno: Turno) {
  const mascota = mascotaStore.mascotas.find((m) => m.id === turno.id_mascota)?.nombre
  const fecha = new Date(turno.fecha_creacion).toLocaleDateString('es-ES')
  const hora = turno.fecha_hora

  const result = await Swal.fire({
    title: '¿Eliminar Turno?',
    html: `
      <p>¿Seguro que quieres eliminar el turno de la mascota?</p>
      <p><strong>${mascota}</strong></p>
      <p>para el dia: ${fecha} a las ${hora} horas</p>
    `,
    iconHtml: '<span style="font-size:40px;color:#dc2626;">🗑️</span>',
    showCancelButton: true,
    confirmButtonText: 'Sí, eliminar',
    cancelButtonText: 'Cancelar',
    confirmButtonColor: '#e11d48',
    cancelButtonColor: '#6b7280',
  })

  if (result.isConfirmed) {
    await confirmarEliminar(turno)
  }
}

async function confirmarEliminar(turno: Turno) {
  await turnoStore.eliminarTurno(turno.id)

  await Swal.fire({
    title: 'Turno Eliminado',
    text: 'El turno fue eliminado correctamente.',
    icon: 'success',
    confirmButtonColor: '#6366f1',
  })
}

function editarTurno(id: number) {
  router.push({ name: 'editarTurno', params: { id } })
}

const formatearFecha = (fecha: string) => {
  return new Date(fecha).toLocaleDateString('es-ES', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}
</script>

<template>
  <div class="page">
    <div class="card">
      <h2 class="title">
        <Icon icon="mdi:clipboard-text-multiple" class="icon" /> Lista de Turnos
        <router-link to="/panel/turnos/crear">
          <Icon icon="mdi:calendar-plus" class="icon" />
        </router-link>
      </h2>

      <div class="table-responsive">
        <table class="table-custom">
          <thead>
            <tr>
              <th>ID</th>
              <th>Mascota</th>
              <th>Veterinario</th>
              <th>Servicio</th>
              <th>Precio</th>
              <th>Fecha</th>
              <th>Hora</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="turno in [...turnoStore.turnos].reverse()" :key="turno.id">
              <td>{{ turno.id }}</td>
              <td>{{ mascotaStore.mascotas.find((m) => m.id === turno.id_mascota)?.nombre }}</td>
              <td>
                {{ usuarioStore.usuarios.find((u) => u.id === turno.id_veterinario)?.nombre }}
                {{ usuarioStore.usuarios.find((u) => u.id === turno.id_veterinario)?.apellido }}
              </td>
              <td>{{ servicioStore.servicios.find((s) => s.id === turno.id_servicio)?.nombre }}</td>
              <td>
                ${{ servicioStore.servicios.find((s) => s.id === turno.id_servicio)?.precio }}
              </td>
              <td>{{ formatearFecha(turno.fecha_creacion) }}</td>
              <td>{{ turno.fecha_hora }}</td>
              <td :class="['estado', turno.estado]">{{ turno.estado }}</td>
              <td class="acciones">
                <button class="btn-action btn-edit" @click="editarTurno(turno.id)">
                  <Icon icon="mdi:paw" class="btn-icon" />
                </button>
                <button class="btn-action btn-delete" @click="abrirModalEliminar(turno)">
                  <Icon icon="mdi:trash-can" class="btn-icon" />
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
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
  max-width: 1000px;
  background: white;
  padding: 35px;
  border-radius: 18px;
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.12);
}

.title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  font-weight: 700;
  margin-bottom: 20px;
}

.icon {
  font-size: 28px;
}

.table-responsive {
  width: 100%;
  overflow-x: auto;
}

.table-custom {
  width: 100%;
  border-collapse: collapse;
  min-width: 800px;
}

.table-custom th,
.table-custom td {
  padding: 12px 15px;
  border-bottom: 1px solid #eee;
  text-align: left;
}

.table-custom th {
  background-color: #6366f1;
  color: white;
  font-weight: 600;
  border-radius: 10px 10px 0 0;
}

.table-custom tr:hover {
  background-color: #f5f5f5;
}

.estado {
  text-transform: uppercase;
  border-radius: 10px;
  text-align: center;
  font-weight: 600;
  padding: 4px 6px;
}

.pendiente {
  background-color: #facc15;
  color: black;
}
.confirmado {
  background-color: #22c55e;
  color: black;
}
.completado {
  background-color: #2563eb;
  color: white;
}

.acciones {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.btn-action {
  border: none;
  cursor: pointer;
  padding: 6px 10px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: 0.2s;
}

.btn-edit {
  background-color: #4f46e5;
}
.btn-edit:hover {
  background-color: #3730a3;
}

.btn-delete {
  background-color: #ef4444;
}
.btn-delete:hover {
  background-color: #b91c1c;
}

.btn-icon {
  font-size: 18px;
  color: white;
}

@media (max-width: 768px) {
  .table-custom th,
  .table-custom td {
    padding: 8px 10px;
    font-size: 12px;
  }

  .btn-icon {
    font-size: 16px;
  }

  .estado {
    font-size: 12px;
    padding: 2px 4px;
  }
}
</style>
