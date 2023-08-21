<template>
  <v-app id="inspire">
    <v-spacer></v-spacer>
    <v-main>
      <v-container>
        <v-row>
          <v-col v-for="(card, key) in cards" :key="key" :sm=" main?6:4" cols="12">
            <a :href="(!main?'admin/':'')+key.toLowerCase()" class="text-decoration-none">
            <v-sheet :height="50" border rounded class="d-flex justify-center align-center">{{card.name}}</v-sheet>
          </a>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<style>
.v-sheet:hover{
  background-color: #cdcdcd;
}
</style>

<script>
 export default {
    name: 'Admin-Main',
    props: {
      cards: Object,
      main: {
        type: Boolean,
        default: false,
    },
 }};
</script>
