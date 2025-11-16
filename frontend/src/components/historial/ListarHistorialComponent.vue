<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useHistorialStore } from '@/stores/historialStore'
import type { Historial } from '@/Interfaces/historialInterface'

const historialStore = useHistorialStore()

const historialAEliminar = ref<Historial | null>(null)
const mostrarModalEliminar = ref(false)

onMounted(async () => {
  await historialStore.obtenerHistoriales()
})

function abrirModalEliminar(historial: Historial) {
  historialAEliminar.value = historial
  mostrarModalEliminar.value = true
}

async function confirmarEliminar() {
  if (historialAEliminar.value) {
    await historialStore.eliminarHistorial(historialAEliminar.value.id)
    mostrarModalEliminar.value = false
  }
}

function verHistorial(historial: Historial) {
  console.log("Ver historial:", historial)
}
</script>

<template>
  <div class="container mt-4">
    <h2>Historial Clínico</h2>

    <table class="table table-striped table-hover">
      <thead class="table-dark">
        <tr>
          <th>ID</th>
          <th>Mascota</th>
          <th>Veterinario</th>
          <th>Fecha</th>
          <th>Diagnóstico</th>
          <th>Acciones</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="h in historialStore.historiales" :key="h.id">
          <td>{{ h.id }}</td>
          <td>{{ h.mascota_nombre}}</td>
          <td>{{ h.veterinario_nombre +" "+ h.veterinario_apellido }}</td>
          <td>{{ new Date(h.fecha).toLocaleDateString('es-ES', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }) }}</td>
          <td>{{ h.diagnostico }}</td>

          <td>
            <button class="btn btn-sm btn-primary me-1" @click="verHistorial(h)">Ver</button>
            <button class="btn btn-sm btn-danger" @click="abrirModalEliminar(h)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal -->
    <div class="modal fade" style="display:block" :class="{ show: mostrarModalEliminar }" v-if="mostrarModalEliminar">
      <div class="modal-dialog">
        <div class="modal-content">

          <div class="modal-header">
            <h5 class="modal-title">Eliminar Historial</h5>
            <button class="btn-close" @click="mostrarModalEliminar=false"></button>
          </div>

          <div class="modal-body">
            <p>¿Eliminar historial del día <strong>{{ new Date(historialAEliminar?.fecha).toLocaleDateString('es-Es',{weekday:'long',year:'numeric',month:'long',day:'numeric'}) }}</strong>?</p>
          </div>

          <div class="modal-footer">
            <button class="btn btn-secondary" @click="mostrarModalEliminar=false">Cancelar</button>
            <button class="btn btn-danger" @click="confirmarEliminar">Eliminar</button>
          </div>

        </div>
      </div>
    </div>

    <div v-if="mostrarModalEliminar" class="modal-backdrop fade show"></div>

  </div>
</template>

<style scoped>
.modal {
  display: block;
}
</style>
