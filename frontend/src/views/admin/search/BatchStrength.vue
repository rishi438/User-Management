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
const name = "Batch Strength";
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
    { title: 'Batch Id', align: 'center', key: 'batch_number' },
    { title: 'Instructor Name', align: 'center', key: 'instructor_name' },
    { title: 'Instructor Email Id', align: 'center', key: 'instructor_email_id' },
    { title: 'Program', align: 'center', key: 'program' },
    { title: 'Category', align: 'center', key: 'category' },
    { title: 'Batch Status', align: 'center', key: 'batch_status' },
    { title: 'Module End Date', align: 'center', key: 'module_end_date' },
];
</script>
