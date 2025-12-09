<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useHistorialStore } from '@/stores/historialStore'
import { useUsuarioStore } from '@/stores/usuarioStore'
import { useMascotaStore } from '@/stores/mascotaStore'
import type { Historial } from '@/Interfaces/historialInterface'
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'
import { Icon } from '@iconify/vue'

const historialStore = useHistorialStore()
const usuarioStore = useUsuarioStore()
const mascotaStore = useMascotaStore()
const router = useRouter()

const historialAEliminar = ref<Historial | null>(null)

onMounted(async () => {
  await usuarioStore.obtenerUsuarios()
  await mascotaStore.obtenerMascotas()
  await historialStore.obtenerHistoriales()
})

async function abrirModalEliminar(historial: Historial) {
  historialAEliminar.value = historial

  const result = await Swal.fire({
    title: '¿Eliminar Historial?',
    html: `
      <p>Estás por eliminar el historial del día:</p>
      <strong>${formatearFecha(historial.fecha)}</strong>
    `,
    iconHtml: '<span style="font-size:40px;color:#dc2626;">🗑️</span>',
    showCancelButton: true,
    confirmButtonText: 'Eliminar',
    cancelButtonText: 'Cancelar',
    confirmButtonColor: '#dc2626',
    cancelButtonColor: '#6b7280',
    backdrop: true,
  })

  if (result.isConfirmed) {
    await confirmarEliminar()
  }
}

async function confirmarEliminar() {
  if (historialAEliminar.value) {
    await historialStore.eliminarHistorial(Number(historialAEliminar.value.id))

    Swal.fire({
      title: 'Eliminado',
      text: 'El historial clínico fue eliminado correctamente.',
      icon: 'success',
      confirmButtonColor: '#4f46e5',
    })
  }
}
function editarHistorial(id: number) {
  router.push({ name: 'editarHistorial', params: { id } })
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
        <Icon icon="mdi:clipboard-text-clock" class="icon" /> Historial Clínico
        <router-link to="/panel/historial/crear" title="Cargar Hitorial nuevo">
          <Icon icon="mdi:clock-plus" class="icon" />
        </router-link>
        <router-link to="/panel/turnos/crear" title="Cargar Turno nuevo">
          <Icon icon="mdi:calendar-plus" class="icon" />
        </router-link>
      </h2>

      <div class="table-responsive">
        <table class="table-custom">
          <thead>
            <tr>
              <th>Mascota</th>
              <th>Veterinario</th>
              <th>Fecha</th>
              <th>Diagnóstico</th>
              <th>Tratamiento</th>
              <th>Observaciones</th>
              <th>Próxima Visita</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="h in historialStore.historiales" :key="h.id">
              <td>{{ mascotaStore.mascotas.find((m) => m.id === h.id_mascota)?.nombre }}</td>
              <td>
                {{
                  usuarioStore.usuarios.find((u) => u.id === h.id_veterinario)?.nombre +
                  ' ' +
                  usuarioStore.usuarios.find((u) => u.id === h.id_veterinario)?.apellido
                }}
              </td>
              <td>{{ formatearFecha(h.fecha) }}</td>
              <td>{{ h.diagnostico }}</td>
              <td>{{ h.tratamiento }}</td>
              <td>{{ h.observaciones }}</td>
              <td>{{ formatearFecha(h.proxima_visita) }}</td>
              <td class="acciones">
                <button class="btn-action btn-edit" @click="editarHistorial(Number(h.id))">
                  <Icon icon="mdi:account-edit" class="btn-icon" />
                </button>
                <button class="btn-action btn-delete" @click="abrirModalEliminar(h)">
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

.acciones {
  display: flex;
  gap: 8px;
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

.modal {
  display: block;
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
}
</style>
