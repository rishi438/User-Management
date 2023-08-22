<template>
    <UploadFile :name="name" :table_headers="headers" />
</template>

<script setup>
import UploadFile from '@/components/UploadFile.vue';
const name = "Upload Multiple Courses";
const headers = [
    { title: 'Product', align: 'center', key: 'product' },
    { title: 'Skills', align: 'center', key: 'skills' },
];
</script>