<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useTurnoStore } from '@/stores/turnoStore'
import type { Turno } from '@/Interfaces/turnoInterface'

const turnoStore = useTurnoStore()

const turnoAEliminar = ref<Turno | null>(null)
const mostrarModalEliminar = ref(false)

onMounted(async () => {
  await turnoStore.obtenerTurnos()
})

function abrirModalEliminar(turno: Turno) {
  turnoAEliminar.value = turno
  mostrarModalEliminar.value = true
}

async function confirmarEliminar() {
  if (turnoAEliminar.value) {
    await turnoStore.eliminarTurno(turnoAEliminar.value.id)
    mostrarModalEliminar.value = false
  }
}

function editarTurno(turno: Turno) {
  console.log('Editar turno:', turno)
}

const formatearFecha = (fecha: string,tipo:string='t') => {
  if (tipo == 'f') {
    return new Date(fecha).toLocaleDateString('es-ES', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
  } else {
    return new Date(fecha).toLocaleTimeString('es-ES', {hour: 'numeric', minute: 'numeric', second: 'numeric' })
  }
}

</script>

<template>
  <div class="container mt-4">
    <h2>Lista de Turnos</h2>

    <table class="table table-striped table-hover">
      <thead class="table-dark">
        <tr>
          <th>ID</th>
          <th>Mascota</th>
          <th>Veterinario</th>
          <th>Fecha</th>
          <th>Hora</th>
          <th>Motivo</th>
          <th>Estado</th>
          <th>Acciones</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="turno in turnoStore.turnos" :key="turno.id">
          <td>{{ turno.id }}</td>
          <td>{{ turno.mascota.nombre }}</td>
          <td>{{ turno.veterinario.nombre + ' ' + turno.veterinario.apellido }}</td>
          <td>{{ formatearFecha(turno.fecha_creacion,'f')}}</td>
          <td>{{ formatearFecha(turno.fecha_hora) }}</td>
          <td>{{ turno.servicio.nombre }}</td>
          <td>{{ turno.estado }}</td>

          <td>
            <button class="btn btn-sm btn-primary me-1" @click="editarTurno(turno)">Editar</button>
            <button class="btn btn-sm btn-danger" @click="abrirModalEliminar(turno)">
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal -->
    <div
      class="modal fade"
      style="display: block"
      :class="{ show: mostrarModalEliminar }"
      v-if="mostrarModalEliminar"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Eliminar Turno</h5>
            <button class="btn-close" @click="mostrarModalEliminar = false"></button>
          </div>

          <div class="modal-body">
            <p>
              ¿Eliminar turno del día <strong>{{ turnoAEliminar?.fecha }}</strong> a las
              <strong>{{ turnoAEliminar?.hora }}</strong
              >?
            </p>
          </div>

          <div class="modal-footer">
            <button class="btn btn-secondary" @click="mostrarModalEliminar = false">
              Cancelar
            </button>
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
