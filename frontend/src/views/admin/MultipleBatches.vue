<template>
    <UploadFile :name="name" :table_headers="headers" />
</template>

<script setup>
import UploadFile from '@/components/UploadFile.vue';
const name = "Upload Multiple Batches";
const headers = [
    { title: 'Batch Id', align: 'center', key: 'batch_id' },
    { title: 'Batch Name', align: 'center', key: 'batch_name' },
    { title: 'Product', align: 'center', key: 'product' },
    { title: 'Product Category', align: 'center', key: 'product_category' },
    { title: 'Go Live Date', align: 'center', key: 'go_live_date' },
    { title: 'Completion Status', align: 'center', key: 'completion_status' },
    { title: 'Days', align: 'center', key: 'days' },
    { title: 'Time', align: 'center', key: 'time' },
    { title: 'Instructor Name', align: 'center', key: 'instructor_name' },
    { title: 'Batch Status', align: 'center', key: 'batch_status' },
    { title: 'Batch Size', align: 'center', key: 'batch_size' },
];
</script>