<template>
  <AdminMain :cards="cards" :main="main" />
</template>

<script setup>
import AdminMain from '@/components/AdminMain.vue';
const cards = {
  "AdminLogin": { name: "Admin Login" },
  "TrainerLogin": { name: "Trainer Login" },
};
const main = true
</script>
