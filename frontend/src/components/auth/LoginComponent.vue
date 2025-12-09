<script setup lang="ts">
import { Icon } from '@iconify/vue'
import useAuthStore from '@/stores/authStore'
import Swal from 'sweetalert2'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const loguearse = async (ev: Event) => {
  ev.preventDefault()

  if (!authStore.usuarioAutorizado.email || !authStore.usuarioAutorizado.password) {
    Swal.fire({
      icon: 'warning',
      title: 'Campos incompletos',
      text: 'Debe completar todos los campos',
    })
    return
  } else {
    await authStore.login(authStore.usuarioAutorizado)
    if (authStore.usuarioAutorizado.rol === 'administrador') {
      router.push({ name: 'panel' })
    } else if (
      authStore.usuarioAutorizado.rol === 'cliente' ||
      authStore.usuarioAutorizado.rol === 'veterinario'
    ) {
      router.push({ name: 'home' })
    }
  }

  const usuario = authStore.usuarioAutorizado

  const esDenegado = usuario.message?.toLowerCase().includes('denegado')

  Swal.fire({
    html: esDenegado
      ? `
        <div style="font-size: 60px; margin-bottom: 10px;">
          ❌
        </div>
        <h2 style="margin: 0; font-size: 22px;">
          Acceso denegado
        </h2>
        <p style="font-size: 16px; margin-top: 5px;">
          Para poder solicitar un turno debes <strong>loguearte</strong>.
        </p>
      `
      : `
        <div style="font-size: 60px; margin-bottom: 10px;">
          👋
        </div>
        <h2 style="margin: 0; font-size: 22px;">
          ${usuario.message || 'Usuario logueado'}
        </h2>
        <p style="font-size: 16px; margin-top: 5px;">
          Bienvenido nuevamente <strong>${usuario.nombre_apellido}</strong>
        </p>
      `,
    timer: 2000,
    showConfirmButton: false,
    padding: '20px',
    backdrop: true,
    allowOutsideClick: false,
    allowEscapeKey: false,
  })
}
</script>

<template>
  <div class="login-bg d-flex justify-content-center align-items-center">
    <form class="card p-4 shadow-lg login-card" @submit="loguearse">
      <div class="text-center mb-4">
        <Icon icon="mdi:paw" width="60" class="text-primary" />
        <h3 class="mt-2 fw-bold text-primary">Veterinaria</h3>
        <p class="text-muted">Acceso al panel administrativo</p>
      </div>

      <div class="mb-3">
        <label for="email" class="form-label fw-semibold">
          <Icon icon="mdi:email-outline" class="me-1 text-primary" />
          Email
        </label>
        <input
          type="text"
          id="email"
          placeholder="Ingresá tu e-mail"
          v-model="authStore.usuarioAutorizado.email"
          class="form-control form-control-lg rounded-3"
        />
      </div>

      <div class="mb-3">
        <label for="pass" class="form-label fw-semibold">
          <Icon icon="mdi:lock-outline" class="me-1 text-primary" />
          Contraseña
        </label>
        <input
          type="password"
          id="pass"
          placeholder="Ingresá tu contraseña"
          v-model="authStore.usuarioAutorizado.password"
          class="form-control form-control-lg rounded-3"
        />
      </div>

      <button
        type="submit"
        class="btn btn-primary w-100 btn-lg rounded-3 mt-3 d-flex justify-content-center align-items-center gap-2"
      >
        <Icon icon="mdi:login" width="22" />
        Iniciar sesión
      </button>
      <router-link
        to="/registrar"
        type="submit"
        class="btn btn-primary w-100 btn-lg rounded-3 mt-3 d-flex justify-content-center align-items-center gap-2"
      >
        <Icon icon="mdi:login" width="22" />
        Registrarse
      </router-link>
    </form>
  </div>
</template>

<style scoped>
.login-bg {
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

.login-card {
  width: 100%;
  max-width: 420px;
  border-radius: 20px;
}
</style>
