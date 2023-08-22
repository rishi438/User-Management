<template>
    <UploadFile :name="name" :table_headers="headers" />
</template>

<script setup>
import UploadFile from '@/components/UploadFile.vue';
const name = "Upload Multiple Students";
const headers = [
    { title: 'Student Id', align: 'center', key: 'student_id' },
    { title: 'Student Name', align: 'center', key: 'student_name' },
    { title: 'Parent Email', align: 'center', key: 'parent_email' },
    { title: 'Parent Number', align: 'center', key: 'parent_number' },
    { title: 'Grade', align: 'center', key: 'grade' },
    { title: 'Product', align: 'center', key: 'product' },
    { title: 'Instructor Id', align: 'center', key: 'instructor_id' },
    { title: 'Instructor Name', align: 'center', key: 'instructor_name' },
    { title: 'Batch Id', align: 'center', key: 'batch_id' },
    { title: 'Batch Name', align: 'center', key: 'batch_name' },
    { title: 'Status', align: 'center', key: 'status' },
];
</script>