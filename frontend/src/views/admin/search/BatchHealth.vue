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
const name = "Batch Health";
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
    { title: 'Instructor Name', align: 'center', key: 'instructor_teacher_name' },
    { title: 'Instructor Email Id', align: 'center', key: 'instructor_email_id' },
    { title: 'Batch Id', align: 'center', key: 'batch_id' },
    { title: 'Program', align: 'center', key: 'program' },
    { title: 'Sessions Delivered For Batch', align: 'center', key: 'sessions_delivered_for_batch' },
    { title: 'Sessions Substituted For Batch', align: 'center', key: 'sessions_delivered_for_batch' },
    { title: 'Sessions Cancelled', align: 'center', key: 'sessions_sancelled' },
];
</script>
