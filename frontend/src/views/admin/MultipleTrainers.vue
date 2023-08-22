<template>
    <UploadFile :name="name" :table_headers="headers" />
</template>

<script setup>
import UploadFile from '@/components/UploadFile.vue';
const name = "Upload Multiple Trainers";
const headers = [
    { title: 'Instructor Id', align: 'center', key: 'instructor_id' },
    { title: 'Instructor Name', align: 'center', key: 'instructor_name' },
    { title: 'Email', align: 'center', key: 'email' },
    { title: 'Mobile Number', align: 'center', key: 'mobile_number' },
    { title: 'Login Name', align: 'center', key: 'login_name' },
];
</script>