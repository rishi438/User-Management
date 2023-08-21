// Composables
import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home.vue'),
      },
      {
        path: '/admin-login',
        name: 'Admin Login',
        component: () => import('@/views/AdminLogin.vue'),
      },
      {
        path: '/trainer-login',
        name: 'Trainer Login',
        component: () => import('@/views/TrainerLogin.vue'),
      },
      {
        path: '/admin-home',
        name: 'Admin-Home',
        component: () => import('@/views/AdminHome.vue'),
      },
    ],
  },
  {
    path:'/admin/',
    component:() => import('@/layouts/admin/Default.vue'),
    children:[

    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
