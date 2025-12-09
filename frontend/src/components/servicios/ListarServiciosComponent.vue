<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useServicioStore } from '@/stores/servicioStore'
import type { Servicio } from '@/Interfaces/servicioInterface'
import { useRouter } from 'vue-router'
import { Icon } from '@iconify/vue'
import Swal from 'sweetalert2'

const servicioStore = useServicioStore()
const servicioAEliminar = ref<Servicio | null>(null)
const router = useRouter()

onMounted(async () => {
  await servicioStore.obtenerServicios()
})

function abrirModalEliminar(servicio: Servicio) {
  servicioAEliminar.value = servicio

  Swal.fire({
    title: '¿Eliminar servicio?',
    html: `<p>¿Estás seguro de eliminar el servicio <strong>${servicio.nombre}</strong>?</p>`,
    iconHtml: '<span style="font-size:40px;color:#dc2626;">🗑️</span>',
    showCancelButton: true,
    confirmButtonColor: '#d33',
    cancelButtonColor: '#3085d6',
    confirmButtonText: 'Sí, eliminar',
    cancelButtonText: 'Cancelar',
  }).then(async (result) => {
    if (result.isConfirmed) {
      await confirmarEliminar()
    }
  })
}

async function confirmarEliminar() {
  if (servicioAEliminar.value) {
    try {
      // Eliminamos el servicio
      await servicioStore.eliminarServicio(servicioAEliminar.value.id)

      // Swal de éxito
      Swal.fire({
        title: 'Eliminado',
        text: 'El servicio fue eliminado correctamente.',
        icon: 'success',
        confirmButtonColor: '#4f46e5',
      })
    } catch (error) {
      // Swal de error
      Swal.fire({
        title: 'Error',
        text: 'Ocurrió un error al eliminar el servicio.',
        icon: 'error',
        confirmButtonColor: '#d33',
      })
    }
  }
}

function editarServicio(id: number) {
  router.push({ name: 'editarServicio', params: { id } })
}
</script>

<template>
  <div class="page">
    <div class="card">
      <h2 class="title">
        <Icon icon="mdi:clipboard-text-outline" class="icon" /> Lista de Servicios
        <router-link to="/panel/servicios/crear">
          <Icon icon="mdi:briefcase-plus" class="icon" />
        </router-link>
      </h2>

      <div class="table-responsive">
        <table class="table-custom">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Descripción</th>
              <th>Precio</th>
              <th>Duración</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="servicio in servicioStore.servicios" :key="servicio.id">
              <td>{{ servicio.id }}</td>
              <td>{{ servicio.nombre }}</td>
              <td>{{ servicio.descripcion }}</td>
              <td>${{ servicio.precio }}</td>
              <td>{{ servicio.duracion_estimada }}</td>
              <td class="acciones">
                <button class="btn-action btn-edit" @click="editarServicio(servicio.id)">
                  <Icon icon="mdi:account-edit" class="btn-icon" />
                </button>
                <button class="btn-action btn-delete" @click="abrirModalEliminar(servicio)">
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
  max-width: 900px;
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
  min-width: 700px;
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
}
</style>
