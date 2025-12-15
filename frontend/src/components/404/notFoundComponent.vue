<script setup lang="ts">
// No necesitas lógica especial aquí
</script>

<template>
  <div class="not-found-container">
    <img
      src="/img/no_encontrado.png"
      alt="Mascota confundida"
      class="not-found-image"
    />
    <h1>404 - Página no encontrada</h1>
    <p>Ups… parece que nuestras mascotas se comieron esta página 🐶🐱</p>
    <router-link to="/" class="home-link">Volver al inicio</router-link>
  </div>
</template>

<style scoped>
.not-found-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 50px 20px;
}

.not-found-image {
  width: 250px;
  max-width: 80%;
  margin-bottom: 20px;
}

h1 {
  font-size: 2rem;
  margin-bottom: 10px;
  color: #ff6b6b;
}

p {
  font-size: 1.2rem;
  margin-bottom: 20px;
  color: #333;
}

.home-link {
  text-decoration: none;
  background-color: #6bc1ff;
  color: white;
  padding: 10px 20px;
  border-radius: 10px;
  font-weight: bold;
  transition: background-color 0.3s;
}

.home-link:hover {
  background-color: #4a90e2;
}
</style>
