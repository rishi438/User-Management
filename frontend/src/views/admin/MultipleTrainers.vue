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
const name = "Upload Multiple Trainers";
const headers = [
    { title: 'Instructor Id', align: 'center', key: 'instructor_id' },
    { title: 'Instructor Name', align: 'center', key: 'instructor_name' },
    { title: 'Email Id', align: 'center', key: 'email_id' },
    { title: 'Mobile Number', align: 'center', key: 'mobile_number' },
    { title: 'Login Name', align: 'center', key: 'login_name' },
];
</script>
