<template>
  <footer class="footer bg-white text-dark shadow-lg mt-5 py-4">
    <div class="container">

      <div class="row text-center text-md-start align-items-center">

        <div class="col-md-4 mb-3 mb-md-0">
          <div class="d-flex align-items-center justify-content-center justify-content-md-start gap-2">
            <Icon icon="mdi:paw" class="footer-logo" />
            <h5 class="mb-0 footer-title">Veterinaria Feliz</h5>
          </div>
          <p class="small text-muted mt-2">
            Cuidamos a tus mejores amigos con amor y dedicación.
          </p>
        </div>

        <div class="col-md-4 mb-3 mb-md-0 text-center">
          <p class="fw-semibold m-0">© 2025 Todos los derechos reservados</p>
          <p class="small text-muted m-0">
            Calle Intentente Francisco San Martin 69 | Tel: 2920286288 | Carmona Ruben Alberto
          </p>
        </div>

        <div class="col-md-4 d-flex justify-content-center justify-content-md-end gap-3">
          <a href="#" class="footer-icon">
            <Icon icon="mdi:facebook" />
          </a>
          <a href="#" class="footer-icon">
            <Icon icon="mdi:instagram" />
          </a>
          <a href="#" class="footer-icon">
            <Icon icon="mdi:twitter" />
          </a>
          <a href="#" class="footer-icon">
            <Icon icon="mdi:youtube" />
          </a>
        </div>

      </div>

    </div>
  </footer>
</template>

<script setup lang="ts">
import { Icon } from "@iconify/vue";
</script>

<style scoped>
.footer {
  border-top: 3px solid #4f46e5;
}

.footer-logo {
  font-size: 32px;
  color: #4f46e5;
}

.footer-title {
  font-weight: 700;
  font-size: 1.25rem;
  color: #111827;
}

/* ICONOS */
.footer-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  color: #4f46e5;
  background: #eef2ff;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  transition: all 0.25s ease;
}

.footer-icon:hover {
  background: #4f46e5;
  color: white;
  transform: translateY(-3px);
  box-shadow: 0 4px 10px rgba(79, 70, 229, 0.3);
}

.small {
  font-size: 0.85rem;
}
</style>
