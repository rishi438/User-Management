<template>
  <v-app-bar flat class="main-nav elevation-5">
    <v-menu transition="slide-y-transition">
      <template v-slot:activator="{ props }">
        <v-btn icon="mdi-menu" v-bind="props" class="d-md-none">
        </v-btn>
      </template>
      <v-list class="d-md-none">
        <div v-for="(sm_items,key) in list" :key="key">
        <v-list-item v-for="(item, key) in sm_items" :key="key" :to="{ name : item.route}">
          <v-list-item-title>{{ item.name }}</v-list-item-title>
        </v-list-item>
      </div>
      </v-list>
    </v-menu>
    <v-row no-gutters class="no-wrap d-none d-md-flex mx-3">
      <div  v-for="(item,key) in list" :key="key" class="mx-2">
        <dropdown-hover :items="item" :main_title="key"/>
      </div >
    </v-row>
  </v-app-bar>
</template>

<style scoped>
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

.v-toolbar-title__placeholder {
  text-wrap: wrap !important;
}
</style>

<script setup>
import DropdownHover from '@/components/DropdownHover.vue';
const list = {
  "Upload":[
    { name: "Multiple Batches",route:"MultipleBatches" },
    { name: "Multiple Courses",route:"MultipleCourses" },
    { name: "Multiple Trainers",route:"MultipleTrainers" },
    { name: "Multiple Students",route:"MultipleStudents" }
  ],
  "View":[
    { name: "View Attendance",route:"ViewAttendance" },
    {name: "View Trainers",route:"ViewTrainers" },
    { name: "View Students",route:"ViewStudents" },
  ],
  "Edit":[
    {name: "Instructor Assign",route:"InstructorAssign" },
    {name: "Change Trainers Batch",route:"ChangeBatchForTrainers" },
    {name: "Change Students Batch",route:"ChangeBatchForStudents" },
  ],
  "Search": [
    {name: "Search All",route:"Search" },
    {name: "Batch Health",route:"BatchHealth" },
    {name: "Batch Strength",route:"BatchStrength" },
    {name: "Students Attendance",route:"StudentsAttendance" },
    {name: "Teacher Payment",route:"TeacherPayment" },
  ],
  "Logout": [{name: "Logout",route:"Home" }],
};
</script>
