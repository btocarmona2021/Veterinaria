<script setup lang="ts">
import { Icon } from '@iconify/vue'
import useAuthStore from '@/stores/authStore'

const authStore = useAuthStore()
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm py-3">
    <div class="container">
      <router-link class="navbar-brand d-flex align-items-center gap-2" to="/" exact>
        <Icon icon="mdi:paw" class="logo-icon" />
        <span class="brand-title">Veterinaria Feliz</span>
      </router-link>

      <button
        class="navbar-toggler border-0 shadow-none"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
      >
        <Icon icon="mdi:menu" class="text-primary fs-2" />
      </button>

      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto align-items-lg-center gap-lg-3">
          <li class="nav-item">
            <router-link class="nav-link nav-link-custom" to="/">
              <Icon icon="mdi:home" class="me-1" />
              Inicio
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link nav-link-custom"
              v-if="authStore.usuarioAutorizado.rol === 'administrador'"
              to="/panel"
            >
              <Icon icon="mdi:view-dashboard" class="me-1" />
              Panel
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-if="!authStore.estaAutorizado"
              class="nav-link nav-link-custom"
              to="/auth/login"
            >
              <Icon icon="mdi:login" class="me-1" />
              Iniciar sesion
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-if="authStore.estaAutorizado"
              @click="authStore.logout"
              class="nav-link nav-link-custom"
              to="/auth/login"
            >
              <Icon icon="mdi:logout" class="me-1" />
              Cerrar sesion
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              v-if="!authStore.estaAutorizado"
              class="nav-link nav-link-custom"
              to="/registrar"
            >
              <Icon icon="mdi:login" class="me-1" />
              Registrar
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.logo-icon {
  font-size: 2rem;
  color: #4f46e5;
  line-height: 1;
}

.brand-title {
  font-weight: 700;
  font-size: 1.25rem;
  color: #111827;
}

.navbar-brand {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.nav-link-custom {
  display: flex;
  align-items: center;
  font-weight: 500;
  padding: 8px 14px !important;
  border-radius: 8px;
  transition: all 0.25s ease;
  color: #374151 !important;
}

.nav-link-custom:hover {
  background: #eef2ff;
  color: #4f46e5 !important;
  transform: translateY(-2px);
}

.navbar-nav .router-link-active {
  background: #4f46e5 !important;
  color: white !important;
  border-radius: 8px;
  box-shadow: 0 3px 10px rgba(79, 70, 229, 0.3);
}

.navbar-nav .router-link-active:hover {
  background: #4338ca !important;
}

@media (max-width: 992px) {
  .nav-link-custom {
    margin-top: 5px;
  }
  .logo-icon {
    font-size: 1.5rem;
  }
  .brand-title {
    font-size: 1rem;
  }
  .navbar-brand {
    gap: 0.25rem;
  }
}
</style>
