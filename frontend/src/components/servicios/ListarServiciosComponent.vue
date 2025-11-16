<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useServicioStore } from '@/stores/servicioStore'
import type { Servicio } from '@/Interfaces/servicioInterface'

const servicioStore = useServicioStore()
const servicioAEliminar = ref<Servicio | null>(null)
const mostrarModalEliminar = ref(false)

onMounted(async () => {
  await servicioStore.obtenerServicios()
})

function abrirModalEliminar(servicio: Servicio) {
  servicioAEliminar.value = servicio
  mostrarModalEliminar.value = true
}

async function confirmarEliminar() {
  if (servicioAEliminar.value) {
    await servicioStore.eliminarServicio(servicioAEliminar.value.id)
    mostrarModalEliminar.value = false
  }
}

function editarServicio(servicio: Servicio) {
  console.log('Editar servicio:', servicio)
}
</script>

<template>
  <div class="container mt-4">
    <h2>Lista de Servicios</h2>

    <table class="table table-striped table-hover">
      <thead class="table-dark">
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
          <td>{{ servicio.precio }}</td>
          <td>{{ servicio.duracion_estimada }}</td>
          <td>
            <button class="btn btn-sm btn-primary me-1" @click="editarServicio(servicio)">Editar</button>
            <button class="btn btn-sm btn-danger" @click="abrirModalEliminar(servicio)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>

    <div class="modal fade" tabindex="-1" :class="{ show: mostrarModalEliminar }" style="display: block;" v-if="mostrarModalEliminar">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Confirmar Eliminación</h5>
            <button type="button" class="btn-close" @click="mostrarModalEliminar=false"></button>
          </div>
          <div class="modal-body">
            <p>¿Estás seguro de eliminar el servicio <strong>{{ servicioAEliminar?.nombre }}</strong>?</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="mostrarModalEliminar=false">Cancelar</button>
            <button type="button" class="btn btn-danger" @click="confirmarEliminar">Eliminar</button>
          </div>
        </div>
      </div>
    </div>
    <div class="modal-backdrop fade show" v-if="mostrarModalEliminar"></div>
  </div>
</template>
