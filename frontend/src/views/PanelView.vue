<script setup lang="ts">
import { onMounted } from 'vue'
import { Icon } from '@iconify/vue'

import { useUsuarioStore } from '@/stores/usuarioStore'
import { useMascotaStore } from '@/stores/mascotaStore'
import { useTurnoStore } from '@/stores/turnoStore'
import { useServicioStore } from '@/stores/servicioStore'
import { useHistorialStore } from '@/stores/historialStore'
import { RouterView } from 'vue-router';

const usuarioStore = useUsuarioStore()
const mascotaStore = useMascotaStore()
const turnoStore = useTurnoStore()
const servicioStore = useServicioStore()
const historialStore = useHistorialStore()

onMounted(async () => {
  await usuarioStore.obtenerUsuarios()
  await mascotaStore.obtenerMascotas()
  await turnoStore.obtenerTurnos()
  await servicioStore.obtenerServicios()
  await historialStore.obtenerHistoriales()
})
</script>

<template>
  <div class="container mt-4">

    <div class="d-flex justify-content-center gap-2 mb-4 flex-wrap">
      <button class="circle-btn btn-primary" @click="$router.push({name:'listarUsuarios'})">
        <Icon icon="mdi:account" width="22" />
        <span>Usuarios</span>
      </button>

      <button class="circle-btn btn-success" @click="$router.push({name:'listarMascotas'})">
        <Icon icon="mdi:dog" width="22" />
        <span>Mascotas</span>
      </button>

      <button class="circle-btn btn-warning" @click="$router.push({name:'listarTurnos'})">
        <Icon icon="mdi:calendar" width="22" />
        <span>Turnos</span>
      </button>

      <button class="circle-btn btn-info" @click="$router.push({name:'listarServicios'})">
        <Icon icon="mdi:toolbox-outline" width="22" />
        <span>Servicios</span>
      </button>

      <button class="circle-btn btn-secondary" @click="$router.push({name:'listarHistorial'})">
        <Icon icon="mdi:clipboard-text-outline" width="22" />
        <span>Historial</span>
      </button>
    </div>

    <div class="stats-row">

      <div class="mini-card gradient-primary" v-if="!usuarioStore.cargando">
        <Icon icon="mdi:account" class="icon" />
        <p class="label">Usuarios</p>
        <p class="value">{{ usuarioStore.usuarios.length }}</p>
      </div>

      <div class="mini-card gradient-success" v-if="!mascotaStore.cargando">
        <Icon icon="mdi:dog" class="icon" />
        <p class="label">Mascotas</p>
        <p class="value">{{ mascotaStore.mascotas.length }}</p>
      </div>

      <div class="mini-card gradient-warning" v-if="!turnoStore.cargando">
        <Icon icon="mdi:calendar" class="icon" />
        <p class="label">Turnos</p>
        <p class="value">{{ turnoStore.turnos.length }}</p>
      </div>

      <div class="mini-card gradient-info" v-if="!servicioStore.cargando">
        <Icon icon="mdi:toolbox-outline" class="icon" />
        <p class="label">Servicios</p>
        <p class="value">{{ servicioStore.servicios.length }}</p>
      </div>

      <div class="mini-card gradient-secondary" v-if="!historialStore.cargando">
        <Icon icon="mdi:clipboard-text-outline" class="icon" />
        <p class="label">Historial</p>
        <p class="value">{{ historialStore.historiales.length }}</p>
      </div>

    </div>

  </div>

  <RouterView />
</template>

<style scoped>

.circle-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  font-size: 14px;
  border-radius: 50px;
  font-weight: 600;
  transition: 0.2s ease;
  border: none;
  cursor: pointer;
}

.circle-btn:hover {
  transform: translateY(-2px);
  filter: brightness(1.1);
}


.stats-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(90px, 1fr));
  gap: 15px;
  justify-items: center;
  margin-bottom: 20px;
}

.mini-card {
  width: 110px;
  height: 110px;
  border-radius: 50%;
  padding: 14px 10px;
  text-align: center;
  color: white;
  box-shadow: 0 4px 12px rgba(0,0,0,0.12);
  transition: 0.25s ease;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.mini-card:hover {
  transform: translateY(-3px);
}

.icon {
  font-size: 30px;
}

.label {
  font-size: 13px;
  margin: 0;
  opacity: 0.9;
}

.value {
  font-size: 20px;
  margin: 0;
  font-weight: bold;
}

/* Móviles */
@media (max-width: 480px) {
  .mini-card {
    width: 85px;
    height: 85px;
  }

  .icon {
    font-size: 22px;
  }

  .value {
    font-size: 16px;
  }

  .label {
    font-size: 11px;
  }
}


.gradient-primary {
  background: linear-gradient(135deg, #3f51b5, #5a6be0);
}

.gradient-success {
  background: linear-gradient(135deg, #4caf50, #66bb6a);
}

.gradient-warning {
  background: linear-gradient(135deg, #ffb300, #ffca28);
  color: #000;
}

.gradient-info {
  background: linear-gradient(135deg, #26c6da, #4dd0e1);
  color: #000;
}

.gradient-secondary {
  background: linear-gradient(135deg, #616161, #757575);
}
</style>
