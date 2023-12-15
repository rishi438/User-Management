<template>
    <BreadCrumbNavigation :navigate_route="navigate_route" class="my-3"/>
    <UploadFile :page_title="name" :table_headers="headers" />
</template>

<script setup>
import UploadFile from '@/components/UploadFile.vue';
import BreadCrumbNavigation from '@/components/BreadCrumbNavigation.vue';
const name = "Upload Multiple Batches";
const headers = [
    { title: 'Batch Id', align: 'center', key: 'batch_id' },
    { title: 'Batch Name', align: 'center', key: 'batch_name' },
    { title: 'Product', align: 'center', key: 'product' },
    { title: 'Product Category', align: 'center', key: 'product_category' },
    { title: 'Go Live Date', align: 'center', key: 'go_live_date' },
    { title: 'Days', align: 'center', key: 'days' },
    { title: 'Time', align: 'center', key: 'time' },
    { title: 'Instructor Name', align: 'center', key: 'instructor_name' },
    { title: 'Batch Status', align: 'center', key: 'batch_status' },
    { title: 'Batch Size', align: 'center', key: 'batch_size' },
];
const navigate_route=[
    {
        title: "home",
        disabled: false,
        href: "home",
    },
    {
        title: name,
        disabled: true,
        href: name,
    },
]
</script>
