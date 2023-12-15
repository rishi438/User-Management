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
const name = "View Trainers";
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
    { title: 'Instructor Id', align: 'center', key: 'instructor_id' },
    { title: 'Instructor Name', align: 'center', key: 'instructor_name' },
    { title: 'Instructor Email Id', align: 'center', key: 'instructor_email_id' },
    { title: 'Instructor Mobile Number', align: 'center', key: 'instructor_mobile_number' },
    { title: 'Created Date', align: 'center', key: 'create_date' },
    { title: 'Updated Date', align: 'center', key: 'updated_date' },
    { title: 'Actions', align: 'center', key: 'actions' },
];
</script>
