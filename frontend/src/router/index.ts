import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ImprintView from '../views/ImprintView.vue'
import PrivacyView from '../views/PrivacyView.vue'
import TermsView from '../views/TermsView.vue'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/tool',
      name: 'tool',
      component: () => import('../views/ToolView.vue'),
    },
    {
      path: '/imprint',
      name: 'imprint',
      component: ImprintView,
    },
    {
      path: '/privacy',
      name: 'privacy',
      component: PrivacyView,
    },
    {
      path: '/terms',
      name: 'terms',
      component: TermsView,
    },
  ],
})

export default router
