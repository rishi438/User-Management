<template>
    <v-app id="inspire1">
       <v-layout align-center justify-center>
        <v-main>
          <v-container>
                <v-flex xs="12" sm="8" md="4">
                   <v-card class="elevation-12">
                      <v-toolbar dark color="primary">
                         <v-toolbar-title>{{login_type}} Login</v-toolbar-title>
                      </v-toolbar>
                      <v-card-text>
                         <v-form>
                            <v-text-field
                               prepend-icon="person"
                               name="login"
                               label="Login"
                               type="text"
                            ></v-text-field>
                            <v-text-field
                               id="password"
                               prepend-icon="lock"
                               name="password"
                               label="Password"
                               type="password"
                            ></v-text-field>
                         </v-form>
                      </v-card-text>
                      <v-card-actions class="mr-2">
                         <v-spacer></v-spacer>
                         <v-btn color="primary" to="/">Login</v-btn>
                      </v-card-actions>
                   </v-card>
                </v-flex>
               </v-container>
            </v-main>
         </v-layout>
    </v-app>
 </template>
 
 <script>
 export default {
    name: 'Main-Login',
    props: {
       source: String,
       login_type:String
    },
 };
 </script>
 