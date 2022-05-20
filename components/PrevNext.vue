<template>
  <v-toolbar flat>
    <v-btn v-if="prev" text outlined :to="{ path: prev.path, params: { slug: prev.slug } }">
      <v-icon left>mdi-chevron-left</v-icon>
      <NuxtLink
        v-if="prev"
        :to="{ path: prev.path, params: { slug: prev.slug } }"
        class="font-bold text-primary hover:underline"
      >
        {{ prev.title }}
      </NuxtLink>
    </v-btn>
    <v-spacer></v-spacer>
    <v-btn v-if="next" text outlined :to="{ path: next.path, params: { slug: next.slug } }">
      <NuxtLink
        v-if="next"
        :to="{ path: next.path, params: { slug: next.slug } }"
        class="font-bold hover:underline"
      >
        {{ next.title }}
      </NuxtLink>
      <v-icon right>mdi-chevron-right</v-icon>
    </v-btn>
  </v-toolbar>
</template>


<script>
  export default {
    props: {
      prev: {
        type: Object,
        default: () => null
      },
      next: {
        type: Object,
        default: () => null
      }
    }
  }
</script>
