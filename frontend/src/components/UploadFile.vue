<template>
  <v-container class="pt-0" fluid>
    <v-row class="pb-3" justify="center">
      <div class="d-flex flex-column my-3">
        <div class="title text-center">
          {{ page_title }}
        </div>
        <v-row>
        <v-file-input class="mx-4 my-4" label="File input" density="compact" @change="on_file_change" @click:clear="on_file_clear"></v-file-input>
        </v-row>
        <div class="mx-auto">
        <v-btn  @click="uploadFile">Upload File</v-btn>
        </div>
      </div>
    </v-row>
    <div class="my-3">
      <data-table ref="data_table" :file_status="file_status" :data="table_data" :headers="table_header" :items_in_page="items_per_page"/>
    </div>
  </v-container>
</template>

<style scoped>
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
    page_title: String,
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
      file_status:false,
    };
  },
  methods: {
    on_file_change(event) {
      this.selected_file = event.target.files[0];
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
              const new_key = key.toLowerCase().replace(/ /g, "_");
              transformed_item[new_key] = item[key];
            }
            return transformed_item;
          });
          this.table_data = formatted_data;
          this.file_status=true;
        };
        reader.readAsArrayBuffer(this.selected_file);
      }
    },
    on_file_clear(){
this.file_status=false;
this.table_data=[];
this.$refs.data_table.clear_fields();
},
    uploadFile() {

    },
  },
};
</script>
