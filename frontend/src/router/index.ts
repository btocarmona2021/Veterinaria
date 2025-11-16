import { createRouter, createWebHistory } from 'vue-router'
import home from '@/views/HomeView.vue'
import PanelView from '@/views/PanelView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: home,
    },
    {
      path: '/panel',
      name: 'panel',
      component: PanelView,
      children: [
        // Usuarios
        {
          path: 'usuarios/crear',
          name: 'crearUsuario',
          component: () => import('@/components/usuarios/CrearUsuarioComponent.vue'),
        },
        {
          path: 'usuarios/listar',
          name: 'listarUsuarios',
          component: () => import('@/components/usuarios/ListarUsuariosComponent.vue'),
        },

        // Mascotas
        {
          path: 'mascotas/crear',
          name: 'crearMascota',
          component: () => import('@/components/mascotas/CrearMascotaComponent.vue'),
        },
        {
          path: 'mascotas/listar',
          name: 'listarMascotas',
          component: () => import('@/components/mascotas/ListarMascotasComponent.vue'),
        },

        // Servicios
        {
          path: 'servicios/crear',
          name: 'crearServicio',
          component: () => import('@/components/servicios/CrearServicioComponent.vue'),
        },
        {
          path: 'servicios/listar',
          name: 'listarServicios',
          component: () => import('@/components/servicios/ListarServiciosComponent.vue'),
        },

        // Turnos
        {
          path: 'turnos/crear',
          name: 'crearTurno',
          component: () => import('@/components/turnos/CrearTurnoComponent.vue'),
        },
        {
          path: 'turnos/listar',
          name: 'listarTurnos',
          component: () => import('@/components/turnos/ListarTurnosComponent.vue'),
        },

        // Historial Médico
        {
          path: 'historial/crear',
          name: 'crearHistorial',
          component: () => import('@/components/historial/CrearHistorialComponent.vue'),
        },
        {
          path: 'historial/listar',
          name: 'listarHistorial',
          component: () => import('@/components/historial/ListarHistorialComponent.vue'),
        },
      ],
    },
  ],
})

export default router

