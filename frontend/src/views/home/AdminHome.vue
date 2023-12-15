<template>
  <AdminMain :cards="cards" :main="main" />
</template>

<script setup>
import AdminMain from '@/components/AdminMain.vue';
const cards = {
  "MultipleBatches": { name: "Multiple Batches" },
  "MultipleCourses": { name: "Multiple Courses" },
  "MultipleTrainers": { name: "Multiple Trainers" },
  "MultipleStudents": { name: "Multiple Students" },
  "ViewAttendance": { name: "View Attendance" },
  "ViewTrainers": { name: "View Trainers" },
  "ViewStudents": { name: "View Students" },
  "InstructorAssign": { name: "Instructor Assign" },
  "ChangeBatchForTrainers": { name: "Change Batch For Trainers" },
  "ChangeBatchForStudents": { name: "Change Batch For Students" },
  "Search": { name: "Search All" },
  "BatchHealth":{name: "Batch Health"},
  "BatchStrength":{name: "Batch Strength"},
  "StudentsAttendance":{name: "Students Attendance"},
  "TeacherPayment":{name: "Teacher Payment"},
  "Home": { name: "Logout" },
};
const main = false;
</script>
