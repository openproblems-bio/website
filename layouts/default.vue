<template>
  <v-app>

    <v-system-bar app color="accent">
       <v-breadcrumbs :class="'primary--text'" :items="crumbs" divider="-" >
          <template v-slot:item="{ item }">
            <v-breadcrumbs-item
              :href="item.href"
              :disabled="item.disabled"
            >
              {{ item.text.toUpperCase() }}
            </v-breadcrumbs-item>
          </template>
        </v-breadcrumbs>
      <v-spacer></v-spacer>
      <span :class="'primary--text'">v{{version}}</span>
    </v-system-bar>

    <v-app-bar app src="/home_hero.jpg" clipped-left>
        <v-img  
          src="/logo.png" max-height="60" contain 
          @click="selected=null;$router.push('/')"
        >
        </v-img>
        <v-spacer></v-spacer>
      <template v-slot:extension>
        <v-tabs 
          fixed-tabs color="secondary" 
          v-model="selected" optional
        >
          <v-tab  v-for="(tab, i) in tabs" :key="i" :to="tab.href">{{tab.text}}</v-tab>
        </v-tabs>
      </template>
    </v-app-bar>
    
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    
    <v-footer fixed app>
      <span> &copy; Open Problems {{ new Date().getFullYear() }}</span>
      <v-spacer></v-spacer>
      <span> View on <a href="https://github.com/openproblems-bio/openproblems">GitHub</a></span>
    </v-footer>
  </v-app>
</template>

<script lang="ts">
import { push_uniq } from "terser"

export default {
  name: 'DefaultLayout',
  data: () => ({ 
    drawer: false,
    items: [],
    title: 'OpenProblems',
    version: '1.0.0',
    tabs: [      
      {
        text: 'Results',
        href: '/results',
        icon: ''
      },
      {
        text: 'NeurIPs',
        href: '/neurips',
        icon: ''
      },      
    ],
    selected:null
  }),
  computed: {
    crumbs () {
      const path: string = this.$route.path
      const parts: string[] = path.split('/')
      const crumbs: Object[] = []
      parts.forEach((text, i) => {
        if (text === '' && i === 0) {
          return crumbs.push({text:'home', disabled:false, href:'/'})
        } else if (text === '') {
          return
        } else {
          let href = []
          for (let j = 0; j < i; j++) {
            href.push(parts[j])
          }
          href.push(text)
          const link = href.join('/')
          console.log(link)
          return crumbs.push({text, disabled:false, href:link})
        }
      })  
      return crumbs     
    }
  }
}
</script>
