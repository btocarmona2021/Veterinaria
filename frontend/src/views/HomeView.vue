<script setup lang="ts">
import { useUsuarioStore } from '@/stores/usuarioStore'
import { useHistorialStore } from '@/stores/historialStore'
import { useMascotaStore } from '@/stores/mascotaStore'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import useAuthStore from '@/stores/authStore';
import Swal from 'sweetalert2'

const usuarioStore = useUsuarioStore()
const historialStore = useHistorialStore()
const mascotaStore = useMascotaStore()
const router = useRouter()
const authStore = useAuthStore()


const reservarTurno = () => {
  if (!authStore.estaAutorizado) {
    Swal.fire({
      icon: 'info',
      title: 'Iniciar sesión',
      text: 'Para solicitar un turno debes iniciar sesión.',
      timer: 2500,
      timerProgressBar: true,
      showConfirmButton: false,
      allowOutsideClick: false,
      allowEscapeKey: false
    }).then(() => {
      router.push({ name: 'login' })
    })
    return
  }
  router.push({ name: 'crearT' })
}

onMounted(async () => {
  await usuarioStore.obtenerUsuarios()
  await historialStore.obtenerHistoriales()
  await mascotaStore.obtenerMascotas()

})
</script>

<template>
  <div>
    <section class="bg-primary text-white text-center py-5">
      <div class="container">
        <h1 class="display-4 fw-bold">Bienvenidos a Nuestra Veterinaria</h1>
        <p class="lead mt-3">
          Cuidamos la salud y felicidad de tus mascotas con profesionalismo y amor.
        </p>
        <button @click="reservarTurno" class="btn btn-light btn-lg mt-3">Solicitar Turno</button>
      </div>
    </section>

    <div id="mainCarousel" class="carousel slide mt-4 container" data-bs-ride="carousel">
      <div class="carousel-inner rounded shadow">
        <div class="carousel-item active">
          <img src="https://placedog.net/1200/400?random=1" class="d-block w-100" alt="slide1" />
        </div>

        <div class="carousel-item">
          <img src="https://placedog.net/1200/400?random" class="d-block w-100" alt="slide2" />
        </div>

        <div class="carousel-item">
          <img src="https://placedog.net/1200/400?random=3" class="d-block w-100" alt="slide3" />
        </div>
      </div>

      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#mainCarousel"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon"></span>
      </button>

      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#mainCarousel"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon"></span>
      </button>
    </div>

    <section class="container my-5">
      <h2 class="text-center mb-4">Nuestros Veterinarios</h2>

      <div class="row g-4">
        <div
          v-for="(v, index) in usuarioStore.usuarios.filter((v) => v.rol == 'veterinario').slice(0,2)"
          :key="index"
          class="col-md-4"
        >
          <div class="card shadow-sm h-100 text-center">
            <img
              :src="`https://i.pravatar.cc/150?img=${v.id +8}`"
              class="card-img-top"
              alt=""
            />
            <div class="card-body">
              <h5 class="card-title">{{ v.nombre + ' ' + v.apellido }}</h5>
              <p class="card-text">
                Se desempenia en nuestro local como: {{ v.especialidad }} incorporado a nuestro
                equipo desde el
                {{
                  new Date(v.fecha_registro).toLocaleString('es-AR', {
                    weekday: 'long',
                    day: 'numeric',
                    month: 'long',
                    year: 'numeric',
                  })
                }}.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="bg-light py-5">
      <div class="container">
        <h2 class="text-center mb-4">Mascotas Felices</h2>

        <div class="row g-4">
          <div
            v-for="(histo, index) in historialStore.historiales.slice(0, 4)"
            :key="index"
            class="col-md-3 col-sm-6"
          >
            <div class="card shadow-sm h-100">
              <img
                :src="
                  mascotaStore.mascotas.find((m) => m.id == histo.id_mascota)?.especie === 'Perro'
                    ? `https://placedog.net/400/400?random=${histo.id_mascota}`
                    : `https://cataas.com/cat?random=${histo.id_mascota}`
                "
                class="card-img-top"
                style="height: 200px; object-fit: cover"
              />

              <div class="card-body">
                <h5 class="card-title text-primary fw-bold">
                  {{ mascotaStore.mascotas.find((m) => m.id == histo.id_mascota)?.nombre }}
                </h5>

                <p class="text-muted small mb-2">
                  {{ mascotaStore.mascotas.find((m) => m.id == histo.id_mascota)?.especie }}
                </p>

                <p class="mb-2">
                  <span class="fw-bold">Ingresó:</span>
                  {{
                    new Date(histo.fecha).toLocaleDateString('es-AR', {
                      day: 'numeric',
                      month: 'long',
                      year: 'numeric',
                    })
                  }}
                </p>

                <p class="mb-1">
                  <span class="fw-bold">Diagnóstico:</span> {{ histo.diagnostico }}
                </p>

                <p class="mb-1">
                  <span class="fw-bold">Tratamiento:</span> {{ histo.tratamiento }}
                </p>

                <p class="mb-0">
                  <span class="fw-bold">Observaciones:</span> {{ histo.observaciones }}
                </p>
              </div>

              <div class="card-footer text-center bg-light">
                <span class="badge bg-secondary">Historial Clínico</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="text-center py-5">
      <h2 class="fw-bold">¿Listo para el próximo control?</h2>
      <p>Agendá un turno con nuestros profesionales.</p>
      <button  @click="reservarTurno" class="btn btn-primary btn-lg">Reservar Ahora</button>
    </section>
  </div>
</template>

<style scoped></style>
