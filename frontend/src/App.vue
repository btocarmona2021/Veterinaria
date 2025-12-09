<script setup lang="ts">
import { RouterView } from 'vue-router'
import HeaderComponent from './components/home/HeaderComponent.vue';
import FooterComponent from './components/home/FooterComponent.vue';
</script>

<template>
  <HeaderComponent />
  <main class="flex-grow-1">
    <router-view />
  </main>

  <FooterComponent />
</template>

<style scoped></style>
