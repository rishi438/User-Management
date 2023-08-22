<template>
  <v-data-table v-bind:items-per-page="items_in_page ? items_in_page : 0" :headers="headers" :items="data"
    class="elevation-1"></v-data-table>
</template>
  
<script>
import { VDataTable } from 'vuetify/labs/VDataTable'
export default {
  components: {
    VDataTable,
  },
  props: {
    headers: Array,
    data: Array,
    items_in_page: Number,
  },
};
</script>