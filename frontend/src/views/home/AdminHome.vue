<template>
  <AdminMain :cards="cards" :main="main" />
</template>

<script setup>
import AdminMain from '@/components/AdminMain.vue';
const cards = {
  "Multiple-Batches": { name: "Multiple Batches" },
  "Multiple-Courses": { name: "Multiple Courses" },
  "Multiple-Trainers": { name: "Multiple Trainers" },
  "Multiple-Students": { name: "Multiple Students" },
  "View-Trainers": { name: "View Trainers" },
  "View-All-Students": { name: "View All Students" },
  "Search": { name: "Search" },
  "Change-Batch-for-Trainers": { name: "Change Batch for Trainers" },
  "Change-Batch-for-Students": { name: "Change Batch for Students" },
  "Instructor-Assign": { name: "Instructor Assign" },
  "View-Attendance": { name: "View Attendance" },
  "Home": { name: "Logout" },
};
const main = false;
</script>
