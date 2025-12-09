<script setup lang="ts">
import { onMounted } from 'vue'
import { useMascotaStore } from '@/stores/mascotaStore'
import type { Mascota } from '@/Interfaces/mascotaInterface'
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'
import { Icon } from '@iconify/vue'
import moment from 'moment'

const mascotaStore = useMascotaStore()
const router = useRouter()

onMounted(async () => {
  await mascotaStore.obtenerMascotas()
})

async function confirmarEliminar(mascota: Mascota) {
  const result = await Swal.fire({
    title: '¿Eliminar mascota?',
    html: `
      <p>Estás por eliminar a <strong>${mascota.nombre}</strong></p>`,
    iconHtml: '<span style="font-size:40px;color:#dc2626;">🗑️</span>',
    showCancelButton: true,
    confirmButtonText: 'Sí, eliminar',
    cancelButtonText: 'Cancelar',
    confirmButtonColor: '#d33',
    cancelButtonColor: '#3085d6',
  })

  if (result.isConfirmed) {
    const respuesta = await mascotaStore.eliminarMascota(mascota.id)
    if (respuesta) {
      Swal.fire({
        title: 'Eliminado',
        text: 'La mascota fue eliminada correctamente.',
        icon: 'success',
        timer: 2000,
        showConfirmButton: false,
      })
    } else {
      Swal.fire({
        title: 'No se ha Eliminado',
        text: 'La mascota no fue eliminada, debe eliminar turnos o historial de la misma, previamente ',
        icon: 'error',
        timer: 3000,
        showConfirmButton: false,
      })
    }
  }
}

function editarMascota(id: number) {
  router.push({ name: 'editarMascota', params: { id } })
}


const calcularEdad = (fecha: Date | string) => {
  const nacimiento = moment(fecha);
  const hoy = moment();

  const años = hoy.diff(nacimiento, "years");
  nacimiento.add(años, "years");

  const meses = hoy.diff(nacimiento, "months");
  nacimiento.add(meses, "months");

  const dias = hoy.diff(nacimiento, "days");
  
const partes: string[] = [];
  if (años > 0) partes.push(`${años} año${años > 1 ? "s" : ""}`);
  if (meses > 0) partes.push(`${meses} mes${meses > 1 ? "es" : ""}`);
  if (dias > 0) partes.push(`${dias} día${dias > 1 ? "s" : ""}`);

  return partes.join(", ").replace(/,([^,]*)$/, " y$1");
};

</script>

<template>
  <div class="page">
    <div class="card">
      <h2 class="title">
        <Icon icon="mdi:dog" class="icon" /> Lista de Mascotas
        <router-link to="/panel/mascotas/crear">
          <Icon icon="mdi:dog-service" class="icon" />
        </router-link>
      </h2>

      <div class="table-responsive">
        <table class="table-custom">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Especie</th>
              <th>Raza</th>
              <th>Edad</th>
              <th>Dueño</th>
              <th>Acciones</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="mascota in mascotaStore.mascotas" :key="mascota.id">
              <td>{{ mascota.id }}</td>
              <td>{{ mascota.nombre }}</td>
              <td>{{ mascota.especie }}</td>
              <td>{{ mascota.raza }}</td>
              <td>{{ calcularEdad(mascota.fecha_nacimiento) }}</td>
              <td>{{ mascota.duenio?.nombre + ' ' + mascota.duenio?.apellido }}</td>

              <td>
                <button class="btn-action btn-edit" @click="editarMascota(mascota.id)">
                  <Icon icon="mdi:pencil" class="btn-icon" />
                </button>

                <button class="btn-action btn-delete" @click="confirmarEliminar(mascota)">
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
  text-align: left;
  border-bottom: 1px solid #eee;
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

.btn-action {
  border: none;
  cursor: pointer;
  padding: 6px 10px;
  margin-right: 5px;
  border-radius: 8px;
  transition: 0.2s;
}

.btn-edit {
  background-color: #4f46e5;
  color: white;
}

.btn-edit:hover {
  background-color: #3730a3;
}

.btn-delete {
  background-color: #ef4444;
  color: white;
}

.btn-delete:hover {
  background-color: #b91c1c;
}

.btn-icon {
  font-size: 18px;
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
