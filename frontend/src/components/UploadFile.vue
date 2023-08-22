<template>
  <v-container fluid>
    <v-row class="py-5" justify="center">
      <div class="d-flex flex-column my-5">
        <div class="title text-center">
          {{ name }}
        </div>
        <v-file-input class="mx-4 my-4" label="File input" density="compact" @change="onFileChange"></v-file-input>
        <v-btn @click="uploadFile">Upload File</v-btn>
      </div>
    </v-row>
    <div class="my-3">
      <data-table :data="table_data" :headers="table_header" :items_in_page="items_per_page" />
    </div>
  </v-container>
</template>
  
<style>
.title {
  font-size: xx-large;
}
</style>
  
<script>
import DataTable from './DataTable.vue';
import { read, utils as XLSXUtils } from 'xlsx';

export default {
  name: 'UploadFile',
  components: {
    DataTable,
  },
  props: {
    name: String,
    table_headers: Array,
  },
  computed: {
    table_header() {
      return this.table_headers;
    },
  },
  data() {
    return {
      table_data: this.table_data,
      items_per_page: 5,
      selected_file: null,
    };
  },
  methods: {
    onFileChange(event) {
      this.selected_file = event.target.files[0];
      console.log(this.table_data)
    },
    uploadFile() {
      if (this.selected_file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          const data = e.target.result;
          const workbook = read(data, { type: 'array' });
          const sheet_name = workbook.SheetNames[0];
          const worksheet = workbook.Sheets[sheet_name];
          const json_data = XLSXUtils.sheet_to_json(worksheet, { header: 0 });
          const formatted_data = json_data.map((item) => {
            const transformed_item = {};
            for (const key in item) {
              console.log(key)
              const new_key = key.toLowerCase().replace(/ /g, "_");
              console.log(new_key)
              transformed_item[new_key] = item[key];
            }
            return transformed_item;
          });
          this.table_data = formatted_data;
          console.log(this.table_data)
        };
        reader.readAsArrayBuffer(this.selected_file);
      }
    },
  },
};
</script>
  