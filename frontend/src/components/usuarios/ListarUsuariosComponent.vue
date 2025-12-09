<script setup lang="ts">
import { onMounted, ref, computed } from 'vue'
import { useUsuarioStore } from '@/stores/usuarioStore'
import type { Usuario } from '@/Interfaces/usuarioInterface'
import { useRouter } from 'vue-router'
import { Icon } from '@iconify/vue'
import Swal from 'sweetalert2'

const usuarioStore = useUsuarioStore()
const router = useRouter()
const busqueda = ref('')

onMounted(async () => {
  await usuarioStore.obtenerUsuarios()
})

function editarUsuario(id: number) {
  router.push({ name: 'editarUsuario', params: { id } })
}

async function abrirModalEliminar(usuario: Usuario) {
  const result = await Swal.fire({
    html: `
      <p>¿Seguro que quieres eliminar el usuario</p>
      <p><strong>${usuario.nombre} ${usuario.apellido}?</strong></p>`,
    iconHtml: '<span style="font-size:40px;color:#dc2626;">🗑️</span>',
    text: '¡Esta acción no se puede deshacer!',
    showCancelButton: true,
    confirmButtonColor: '#ef4444',
    cancelButtonColor: '#6b7280',
    confirmButtonText: 'Sí, eliminar',
    cancelButtonText: 'Cancelar',
  })

  if (result.isConfirmed) {
    const respuesta = await usuarioStore.eliminarUsuario(usuario.id)
    if (respuesta) {
      Swal.fire({
        title: 'Eliminado',
        text: 'El usuario ha sido eliminado correctamente.',
        icon: 'success',
        timer: 2000,
        showConfirmButton: false,
      })
    } else {
      Swal.fire({
        title: 'No se ha Eliminado',
        text: 'El usuario no se ha podido eliminar, debe eliminar turnos o historial previamente',
        icon: 'error',
        timer: 2000,
        showConfirmButton: false,
      })
    }
  }
}

const usuariosFiltrados = computed(() => {
  const txt = busqueda.value.trim().toLowerCase()
  if (!txt) return usuarioStore.usuarios

  return usuarioStore.usuarios.filter(
    (u) => u.email.toLowerCase().includes(txt) || u.telefono.toLowerCase().includes(txt),
  )
})
</script>

<template>
  <div class="page">
    <div class="card">
      <h2 class="title">
        <Icon icon="mdi:account-multiple" class="icon" /> Lista de Usuarios
        <router-link to="/panel/usuarios/crear">
          <Icon icon="mdi:account-plus" class="icon" />
        </router-link>
      </h2>

      <div class="filter-box">
        <Icon icon="mdi:magnify" class="search-icon" />
        <input
          type="text"
          v-model="busqueda"
          placeholder="Buscar por email o teléfono..."
          class="filter-input"
        />
      </div>

      <table class="table-custom">
        <thead>
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
          <tr v-for="usuario in usuariosFiltrados" :key="usuario.id">
            <td>{{ usuario.id }}</td>
            <td>{{ usuario.nombre }}</td>
            <td>{{ usuario.apellido }}</td>
            <td>{{ usuario.email }}</td>
            <td>{{ usuario.telefono }}</td>
            <td>{{ usuario.rol }}</td>
            <td>
              <button class="btn-action btn-edit" @click="editarUsuario(usuario.id)">
                <Icon icon="mdi:account-edit" class="btn-icon" />
              </button>

              <button class="btn-action btn-delete" @click="abrirModalEliminar(usuario)">
                <Icon icon="mdi:trash-can" class="btn-icon" />
              </button>
            </td>
          </tr>
        </tbody>
      </table>
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
  box-sizing: border-box;
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

.filter-box {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 15px;
  background: #f3f4f6;
  padding: 10px 15px;
  border-radius: 10px;
}

.filter-input {
  width: 100%;
  border: none;
  background: transparent;
  outline: none;
  font-size: 15px;
}

.search-icon {
  font-size: 22px;
  color: #4b5563;
}

.table-custom {
  width: 100%;
  border-collapse: collapse;
  display: block;
  overflow-x: auto;
}

.table-custom th,
.table-custom td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #eee;
  white-space: nowrap;
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

.modal {
  display: block;
}

@media (max-width: 768px) {
  .table-custom th,
  .table-custom td {
    padding: 10px 8px;
  }
}

@media (max-width: 480px) {
  .table-custom {
    font-size: 14px;
  }

  .btn-action {
    padding: 4px 6px;
  }

  .btn-icon {
    font-size: 16px;
  }
}
</style>
