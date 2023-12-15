<template>
    <BreadCrumbNavigation :navigate_route="navigate_route" class="my-3"/>
    <data-table ref="data_table" :data="table_data" :headers="table_header" :items_in_page="items_per_page"/>
</template>

<script setup>
import DataTable from '@/components/DataTable.vue';
import BreadCrumbNavigation from '@/components/BreadCrumbNavigation.vue';
DataTable;
const table_data=[];
const items_per_page=5;
const name = "Change Students Batch";
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
const table_header = [
    { title: 'Student Id', align: 'center', key: 'student_id' },
    { title: 'Student Name', align: 'center', key: 'student_name' },
    { title: 'Parent Email id', align: 'center', key: 'parent_email_id' },
    { title: 'Parent Mobile Number', align: 'center', key: 'parent_mobile_number' },
    { title: 'Grade', align: 'center', key: 'grade' },
    { title: 'Product', align: 'center', key: 'product' },
    { title: 'Instructor Id', align: 'center', key: 'instructor_id' },
    { title: 'Instructor Name', align: 'center', key: 'instructor_name' },
    { title: 'Batch Id', align: 'center', key: 'batch_id' },
    { title: 'Batch Name', align: 'center', key: 'batch_name' },
    { title: 'Status', align: 'center', key: 'status' },
    { title: 'Actions', align: 'center', key: 'actions' },
];
</script>
