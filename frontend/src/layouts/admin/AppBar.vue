<template>
  <v-app-bar flat class="main-nav elevation-5">
    <v-menu transition="slide-y-transition">
      <template v-slot:activator="{ props }">
        <v-btn icon="mdi-menu" v-bind="props" class="d-md-none">
        </v-btn>
      </template>
      <v-list offset-y="10">
        <v-list-item v-for="(item, key) in list" :key="key" :to="{ name: key.replaceAll('-', '') }">
          <v-list-item-title>{{ item.name }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <v-row no-gutters class="no-wrap d-none d-md-flex justify-md-space-around mx-3">
      <router-link v-for="(item, key) in list" :key="key" :to="{ name: key.replaceAll('-', '') }"
        class="d-none d-md-flex text-decoration-none title my-2 align-self-center rounded text-center">
        <v-app-bar-title class="mx-1">
          {{ item.name }}
        </v-app-bar-title>
      </router-link>
    </v-row>
  </v-app-bar>
</template>

<style>
.no-wrap {
  flex-wrap: unset !important;
}

.main-nav {
  background-color: #3f3f3f !important;
  color: #fff !important;
}

.v-app-bar-title {
  font-size: small !important;
}

.main-nav .title:hover {
  color: #ffffff !important;
  background-color: #565656;
}

.v-toolbar-title__placeholder {
  text-wrap: wrap !important;
}
</style>

<script setup>
const list = {
  "Multiple-Batches": { name: "Multiple Batches" },
  "Multiple-Courses": { name: "Multiple Courses" },
  "Multiple-Trainers": { name: "Multiple Trainers" },
  "Multiple-Students": { name: "Multiple Students" },
  "View-Trainers": { name: "View Trainers" },
  "View-All-Students": { name: "View All Students" },
  "Search-Student": { name: "Search Student" },
  "Change-Batch-for-Trainers": { name: "Edit Trainers Batch" },
  "Change-Batch-for-Students": { name: "Edit Students Batch" },
  "Instructor-Assign": { name: "Instructor Assign" },
  "View-Attendance": { name: "View Attendance" },
  "Logout": { name: "Home" },
};
</script>
