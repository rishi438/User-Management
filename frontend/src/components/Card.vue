<template>
  <v-card class="mx-auto py-3 elevation-5" max-width="344" variant="outlined">
    <v-card-item>
      <v-form @submit.prevent>
        <v-autocomplete
          class="px-0"
          clearable
          label="Select Field"
          :items="search_parms"
          v-model="search_parm"
          @click:clear="clear_text"
        ></v-autocomplete>
        <v-text-field
          clearable
          :label="`${search_parm?'Enter '+search_parm:'Disabled'}`"
          :rules="[(value) => {
            if (value) {
              btn_state = search_parm?true:false;
              return true;
            } else {
              btn_state = false
              return 'This field is required';
            }
          }]"
          :disabled="!search_parm"
          :lazy="true"
          @click:clear="btn_state=false"
          ref="second_field"
        ></v-text-field>
        <v-btn class="ml-3" variant="outlined" :disabled="!btn_state"> Search </v-btn>
      </v-form>
    </v-card-item>
  </v-card>
</template>

<script>
export default {
  props: {
    search_parms: Array,
  },
  data: () => ({
    search_parm: null,
    btn_state: false,
  }),
  methods: {
    clear_text(){
      this.$refs.second_field.reset()
      this.$refs.second_field.resetValidation()
    }
  },
}
</script>
