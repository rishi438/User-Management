<template>
    <BreadCrumbNavigation :navigate_route="navigate_route" class="my-3"/>
    <v-container class="my-5">
        <div class="title text-center">
            Search Information
          </div>
        <card class="my-5" :search_parms="search_list"/>
    </v-container>
</template>

<style scoped>
.title{
    font-size: xx-large;
}
</style>

<script setup>
import Card from '@/components/Card.vue';
import BreadCrumbNavigation from '@/components/BreadCrumbNavigation.vue';
const name = "Search";
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
const search_list=["Student Name","Student Id","Batch Name","Instructor Name","Batch Status"]
</script>
