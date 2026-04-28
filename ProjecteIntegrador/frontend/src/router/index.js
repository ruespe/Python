import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import GameView from '../views/GameView.vue'
import HistoryView from '../views/HistoryView.vue'

const routes = [
  { path: '/', redirect: '/joc' },
  { path: '/login', component: LoginView },
  { path: '/joc', component: GameView, meta: { requiresAuth: true } },
  { path: '/historial', component: HistoryView, meta: { requiresAuth: true } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// Guard de navegació: protegeix les rutes que requereixen autenticació
router.beforeEach(async (to) => {
  if (to.meta.requiresAuth) {
    const res = await fetch('/api/auth/me/')
    const data = await res.json()
    if (!data.authenticated) {
      return '/login'
    }
  }
})

export default router
