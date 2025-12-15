import { createRouter, createWebHistory } from 'vue-router'
import home from '@/views/HomeView.vue'
import PanelView from '@/views/PanelView.vue'
import LoginView from '@/views/LoginView.vue'
import useAuthStore from '@/stores/authStore'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: home,
    },
    {
      path: '/auth/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/crearturno',
      name: 'crearT',
      component: () => import('@/components/turnos/CrearTurnoComponent.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/registrar',
      name: 'registrar',
      component: () => import('@/components/usuarios/CrearUsuarioComponent.vue'),
    },
    {
      path: '/panel',
      name: 'panel',
      component: PanelView,
      meta: { requiresAuth: true, roles: ['administrador', 'veterinario'] },
      children: [
        // Usuarios
        {
          path: 'usuarios/crear',
          name: 'crearUsuario',
          component: () => import('@/components/usuarios/CrearUsuarioComponent.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'usuarios/listar',
          name: 'listarUsuarios',
          component: () => import('@/components/usuarios/ListarUsuariosComponent.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'usuarios/editar/:id',
          name: 'editarUsuario',
          component: () => import('@/components/usuarios/EditarUsuarioComponent.vue'),
          meta: { requiresAuth: true },
        },

        // Mascotas
        {
          path: 'mascotas/crear',
          name: 'crearMascota',
          component: () => import('@/components/mascotas/CrearMascotaComponent.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'mascotas/listar',
          name: 'listarMascotas',
          component: () => import('@/components/mascotas/ListarMascotasComponent.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'mascotas/editar/:id',
          name: 'editarMascota',
          component: () => import('@/components/mascotas/EditarMascotaComponent.vue'),
          meta: { requiresAuth: true },
        },

        {
          path: 'servicios/crear',
          name: 'crearServicio',
          component: () => import('@/components/servicios/CrearServicioComponent.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'servicios/listar',
          name: 'listarServicios',
          component: () => import('@/components/servicios/ListarServiciosComponent.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'servicios/editar/:id',
          name: 'editarServicio',
          component: () => import('@/components/servicios/EditarServicioComponent.vue'),
          meta: { requiresAuth: true },
        },

        // Turnos
        {
          path: 'turnos/crear',
          name: 'crearTurno',
          component: () => import('@/components/turnos/CrearTurnoComponent.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'turnos/listar',
          name: 'listarTurnos',
          component: () => import('@/components/turnos/ListarTurnosComponent.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'turnos/editar/:id',
          name: 'editarTurno',
          component: () => import('@/components/turnos/EditarTurnoComponent.vue'),
          meta: { requiresAuth: true },
        },

        // Historial
        {
          path: 'historial/crear',
          name: 'crearHistorial',
          component: () => import('@/components/historial/CrearHistorialComponent.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'historial/listar',
          name: 'listarHistorial',
          component: () => import('@/components/historial/ListarHistorialComponent.vue'),
          meta: { requiresAuth: true },
        },
        {
          path: 'historial/editar/:id',
          name: 'editarHistorial',
          component: () => import('@/components/historial/EditarHistorialComponent.vue'),
          meta: { requiresAuth: true },
        },
      ],
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('@/components/404/notFoundComponent.vue'),
    },
  ],
})

router.beforeEach((to, from, next) => {

  const authStore = useAuthStore()
  const meta = to.meta as { requiresAuth?: boolean; roles?: string[] }

  if (meta.requiresAuth && !authStore.estaAutorizado) {
    return next({ name: 'login' })
  }


  if (meta.roles) {
    const rolUsuario = authStore.usuarioAutorizado.rol

    if (!meta.roles.includes(rolUsuario)) {
      return next({ name: 'home' })
    }
  }

  next()
})

export default router
