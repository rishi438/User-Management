<template>
  <v-app id="inspire">
    <v-spacer></v-spacer>
    <v-main>
      <v-container>
        <v-row>
          <v-col v-for="(card, key) in cards" :key="key" sm="4" cols="12">
            <a href="" class="text-decoration-none">
            <v-sheet :height="50" border rounded class="d-flex justify-center align-center">{{card.name}}</v-sheet>
          </a>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      cards: {
        "Multiple Trainer": { name: "Trainers" },
        "Multiple Students": { name: "Students" },
        "Multiple Instructors": { name: "Instructors" },
        "Multiple Batches": { name: "Batches" },
      },
    };
  },
};
</script>
