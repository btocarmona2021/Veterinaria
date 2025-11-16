<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useUsuarioStore } from '@/stores/usuarioStore'
import type { Usuario } from '@/Interfaces/usuarioInterface'

const usuarioStore = useUsuarioStore()

// Para confirmar eliminación
const usuarioAEliminar = ref<Usuario | null>(null)
const mostrarModalEliminar = ref(false)

// Cargar usuarios al montar el componente
onMounted(async () => {
  await usuarioStore.obtenerUsuarios()
})

// Función para abrir modal de eliminación
function abrirModalEliminar(usuario: Usuario) {
  usuarioAEliminar.value = usuario
  mostrarModalEliminar.value = true
}

// Confirmar eliminación
async function confirmarEliminar() {
  if (usuarioAEliminar.value) {
    await usuarioStore.eliminarUsuario(usuarioAEliminar.value.id)
    mostrarModalEliminar.value = false
  }
}

// Función para editar usuario
function editarUsuario(usuario: Usuario) {
  // Aquí podrías navegar a un formulario de edición o abrir un modal
  console.log('Editar usuario:', usuario)
}
</script>

<template>
  <div class="container mt-4">
    <h2>Lista de Usuarios</h2>

    <table class="table table-striped table-hover">
      <thead class="table-dark">
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>Apellido</th>
          <th>Email</th>
          <th>Teléfono</th>
          <th>Rol</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="usuario in usuarioStore.usuarios" :key="usuario.id">
          <td>{{ usuario.id }}</td>
          <td>{{ usuario.nombre }}</td>
          <td>{{ usuario.apellido }}</td>
          <td>{{ usuario.email }}</td>
          <td>{{ usuario.telefono }}</td>
          <td>{{ usuario.rol }}</td>
          <td>
            <button class="btn btn-sm btn-primary me-1" @click="editarUsuario(usuario)">Editar</button>
            <button class="btn btn-sm btn-danger" @click="abrirModalEliminar(usuario)">Eliminar</button>
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
            <p>¿Estás seguro de eliminar al usuario <strong>{{ usuarioAEliminar?.nombre }} {{ usuarioAEliminar?.apellido }}</strong>?</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="mostrarModalEliminar=false">Cancelar</button>
            <button type="button" class="btn btn-danger" @click="confirmarEliminar">Eliminar</button>
          </div>
        </div>
      </div>
    </div>
    <!-- Fondo modal -->
    <div class="modal-backdrop fade show" v-if="mostrarModalEliminar"></div>
  </div>
</template>

<style scoped>
.modal {
  display: block; /* para que sea visible cuando mostramos */
}
</style>
