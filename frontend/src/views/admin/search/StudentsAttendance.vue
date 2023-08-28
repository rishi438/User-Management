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
const name = "Students Attendance";
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
    { title: 'Grade', align: 'center', key: 'grade' },
    { title: 'Program', align: 'center', key: 'product' },
    { title: 'Batch Id', align: 'center', key: 'batch_id' },
    { title: 'Classes Conducted', align: 'center', key: 'classes_conducted' },
    { title: 'Classes Present', align: 'center', key: 'classes_present' },
    { title: 'Attendance Percentage', align: 'center', key: 'attendance_percentage' },
];
</script>
