<template>
  <AdminMain :cards="cards" :main="main"/>
</template>

<script setup>
import AdminMain from '@/components/AdminMain.vue';
const cards = {
"Admin-Login": { name: "Admin Login" },
"Trainer-Login": { name: "Trainer Login" },
};
const main=true
</script>
