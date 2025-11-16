<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useUsuarioStore } from '@/stores/usuarioStore'
import { useMascotaStore } from '@/stores/mascotaStore'
import { useTurnoStore } from '@/stores/turnoStore'
import { useServicioStore } from '@/stores/servicioStore'

const usuarioStore = useUsuarioStore()
const mascotaStore = useMascotaStore()
const turnoStore = useTurnoStore()
const servicioStore = useServicioStore()

// Cargar datos al iniciar
onMounted(async () => {
  await usuarioStore.obtenerUsuarios()
  await mascotaStore.obtenerMascotas()
  await turnoStore.obtenerTurnos()
  await servicioStore.obtenerServicios()
})
</script>

<template>
  <div class="container mt-5">

    <!-- Título -->
    <h1 class="text-center mb-4">Bienvenido a la Veterinaria</h1>

    <!-- Botones rápidos -->
    <div class="d-flex justify-content-center gap-3 mb-5 flex-wrap">
      <button class="btn btn-primary" @click="$router.push('/usuarios')">Usuarios</button>
      <button class="btn btn-success" @click="$router.push('/mascotas')">Mascotas</button>
      <button class="btn btn-warning" @click="$router.push('/turnos')">Turnos</button>
      <button class="btn btn-info text-white" @click="$router.push('/servicios')">Servicios</button>
      <button class="btn btn-secondary" @click="$router.push('/historial')">Historial Médico</button>
    </div>

    <!-- Resumen rápido con Cards -->
    <div class="row g-4">
      <div class="col-md-3" v-if="!usuarioStore.cargando">
        <div class="card text-white bg-primary h-100">
          <div class="card-body">
            <h5 class="card-title">Usuarios</h5>
            <p class="card-text fs-3">{{ usuarioStore.usuarios.length }}</p>
          </div>
        </div>
      </div>

      <div class="col-md-3" v-if="!mascotaStore.cargando">
        <div class="card text-white bg-success h-100">
          <div class="card-body">
            <h5 class="card-title">Mascotas</h5>
            <p class="card-text fs-3">{{ mascotaStore.mascotas.length }}</p>
          </div>
        </div>
      </div>

      <div class="col-md-3" v-if="!turnoStore.cargando">
        <div class="card text-white bg-warning h-100">
          <div class="card-body">
            <h5 class="card-title">Turnos</h5>
            <p class="card-text fs-3">{{ turnoStore.turnos.length }}</p>
          </div>
        </div>
      </div>

      <div class="col-md-3" v-if="!servicioStore.cargando">
        <div class="card text-white bg-info h-100">
          <div class="card-body">
            <h5 class="card-title">Servicios</h5>
            <p class="card-text fs-3">{{ servicioStore.servicios.length }}</p>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
h1 {
  color: #2c3e50;
}
.card {
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
</style>
