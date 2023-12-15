// Composables
import {createRouter, createWebHistory} from "vue-router";

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
        component: () => import("@/views/admin/upload/MultipleBatches.vue"),
      },
      {
        path: "multiple-courses",
        name: "MultipleCourses",
        component: () => import("@/views/admin/upload/MultipleCourses.vue"),
      },
      {
        path: "multiple-trainers",
        name: "MultipleTrainers",
        component: () => import("@/views/admin/upload/MultipleTrainers.vue"),
      },
      {
        path: "multiple-students",
        name: "MultipleStudents",
        component: () => import("@/views/admin/upload/MultipleStudents.vue"),
      },
      {
        path: "view-attendance",
        name: "ViewAttendance",
        component: () => import("@/views/admin/view/ViewAttendance.vue"),
      },
      {
        path: "view-trainers",
        name: "ViewTrainers",
        component: () => import("@/views/admin/view/ViewTrainers.vue"),
      },
      {
        path: "view-students",
        name: "ViewStudents",
        component: () => import("@/views/admin/view/ViewStudents.vue"),
      },
      {
        path: "instructor-assign",
        name: "InstructorAssign",
        component: () => import("@/views/admin/edit/InstructorAssign.vue"),
      },
      {
        path: "change-batch-for-trainers",
        name: "ChangeBatchForTrainers",
        component: () => import("@/views/admin/edit/ChangeBatchForTrainers.vue"),
      },
      {
        path: "change-batch-for-students",
        name: "ChangeBatchForStudents",
        component: () => import("@/views/admin/edit/ChangeBatchForStudents.vue"),
      },
      {
        path: "search",
        name: "Search",
        component: () => import("@/views/admin/search/SearchAll.vue"),
      },
      {
        path: "batch-health",
        name: "BatchHealth",
        component: () => import("@/views/admin/search/BatchHealth.vue"),
      },
      {
        path: "batch-strength",
        name: "BatchStrength",
        component: () => import("@/views/admin/search/BatchStrength.vue"),
      },
      {
        path: "students-attendance",
        name: "StudentsAttendance",
        component: () => import("@/views/admin/search/StudentsAttendance.vue"),
      },
      {
        path: "teacher-payment",
        name: "TeacherPayment",
        component: () => import("@/views/admin/search/TeacherPayment.vue"),
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
