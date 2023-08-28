<template>
    <BreadCrumbNavigation :navigate_route="navigate_route" class="my-3"/>
    <UploadFile :page_title="name" :table_headers="headers" />
</template>

<script setup>
import UploadFile from '@/components/UploadFile.vue';
import BreadCrumbNavigation from '@/components/BreadCrumbNavigation.vue';
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
const name = "Upload Multiple Students";
const headers = [
    { title: 'Student Id', align: 'center', key: 'student_id' },
    { title: 'Student Name', align: 'center', key: 'student_name' },
    { title: 'Parent Email Id', align: 'center', key: 'parent_email_id' },
    { title: 'Parent Mobile Number', align: 'center', key: 'parent_mobile_number' },
    { title: 'Grade', align: 'center', key: 'grade' },
    { title: 'Product', align: 'center', key: 'product' },
    { title: 'Instructor Id', align: 'center', key: 'instructor_id' },
    { title: 'Instructor Name', align: 'center', key: 'instructor_name' },
    { title: 'Batch Id', align: 'center', key: 'batch_id' },
    { title: 'Batch Name', align: 'center', key: 'batch_name' },
    { title: 'Status', align: 'center', key: 'status' },
];
</script>
