<!-- ListarMascotasComponent.vue -->
<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useMascotaStore } from '@/stores/mascotaStore'
import type { Mascota } from '@/Interfaces/mascotaInterface'

const mascotaStore = useMascotaStore()

const mascotaAEliminar = ref<Mascota | null>(null)
const mostrarModalEliminar = ref(false)

onMounted(async () => {
  await mascotaStore.obtenerMascotas()
})

function abrirModalEliminar(mascota: Mascota) {
  mascotaAEliminar.value = mascota
  mostrarModalEliminar.value = true
}

async function confirmarEliminar() {
  if (mascotaAEliminar.value) {
    await mascotaStore.eliminarMascota(mascotaAEliminar.value.id)
    mostrarModalEliminar.value = false
  }
}

function editarMascota(mascota: Mascota) {
  console.log('Editar mascota:', mascota)
}
</script>

<template>
  <div class="container mt-4">
    <h2>Lista de Mascotas</h2>

    <table class="table table-striped table-hover">
      <thead class="table-dark">
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
          <td>{{ mascota.edad }}</td>
          <td>{{ mascota.id_usuario }}</td>
          <td>
            <button class="btn btn-sm btn-primary me-1" @click="editarMascota(mascota)">Editar</button>
            <button class="btn btn-sm btn-danger" @click="abrirModalEliminar(mascota)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal de confirmación -->
    <div class="modal fade" tabindex="-1" :class="{ show: mostrarModalEliminar }" style="display: block;" v-if="mostrarModalEliminar">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Confirmar Eliminación</h5>
            <button type="button" class="btn-close" @click="mostrarModalEliminar=false"></button>
          </div>
          <div class="modal-body">
            <p>¿Estás seguro de eliminar a la mascota <strong>{{ mascotaAEliminar?.nombre }}</strong>?</p>
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

<style scoped>
.modal {
  display: block;
}
</style>
