// Composables
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("@/layouts/default/Default.vue"),
    children: [
      {
        path: "",
        name: "Home",
        component: () => import("@/views/home/Home.vue"),
      },
      {
        path: "admin",
        name: "AdminLogin",
        component: () => import("@/views/home/AdminLogin.vue"),
      },
      {
        path: "trainer",
        name: "TrainerLogin",
        component: () => import("@/views/home/TrainerLogin.vue"),
      },
    ],
  },
  {
    path: "/admin",
    components: {
      default: () => import("@/layouts/admin/Default.vue"),
    },
    children: [
      {
        path: "multiple-batches",
        name: "MultipleBatches",
        component: () => import("@/views/admin/MultipleBatches.vue"),
      },
      {
        path: "multiple-courses",
        name: "MultipleCourses",
        component: () => import("@/views/admin/MultipleCourses.vue"),
      },
      {
        path: "multiple-trainers",
        name: "MultipleTrainers",
        component: () => import("@/views/admin/MultipleTrainers.vue"),
      },
      {
        path: "multiple-students",
        name: "MultipleStudents",
        component: () => import("@/views/admin/MultipleStudents.vue"),
      },
      {
        path: "view-trainers",
        name: "ViewTrainers",
        component: () => import("@/views/admin/MultipleBatches.vue"),
      },
      {
        path: "view-all-students",
        name: "ViewAllStudents",
        component: () => import("@/views/admin/MultipleBatches.vue"),
      },
      {
        path: "search-student",
        name: "SearchStudent",
        component: () => import("@/views/admin/MultipleBatches.vue"),
      },
      {
        path: "change-batch-for-trainers",
        name: "ChangeBatchforTrainers",
        component: () => import("@/views/admin/MultipleBatches.vue"),
      },
      {
        path: "change-batch-for-students",
        name: "ChangeBatchforStudents",
        component: () => import("@/views/admin/MultipleBatches.vue"),
      },
      {
        path: "instructor-assign",
        name: "InstructorAssign",
        component: () => import("@/views/admin/MultipleBatches.vue"),
      },
      {
        path: "view-attendance",
        name: "ViewAttendance",
        component: () => import("@/views/admin/MultipleBatches.vue"),
      },
    ],
  },
  {
    path: "/admin/home",
    components: {
      default: () => import("@/layouts/default/Default.vue"),
    },
    children: [
      {
        path: "",
        name: "AdminHome",
        component: () => import("@/views/home/AdminHome.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
