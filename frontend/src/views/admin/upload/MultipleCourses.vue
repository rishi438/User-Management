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
const name = "Upload Multiple Courses";
const headers = [
    { title: 'Product', align: 'center', key: 'product' },
    { title: 'Skills', align: 'center', key: 'skills' },
];
</script>
