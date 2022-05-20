<template>
  <div>
    <v-card
      max-width="600"
      class="mx-auto"
    >
      <v-toolbar
        color="primary"
        dark
      >
        <v-toolbar-title>Articles</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-text-field
          hide-details
          append-icon="mdi-magnify"
          single-line
          v-model="query" type="search" autocomplete="off" 
        ></v-text-field>
      </v-toolbar>
      <v-list>
        <v-list-item v-for="article of searched" :key="article.slug">
            <NuxtLink :to="{ path: `${article.path}` }">
              <v-list-item-content>
                <v-list-item-title v-text="article.title"></v-list-item-title>
              </v-list-item-content>
            </NuxtLink>
        </v-list-item>
      </v-list>
    </v-card>

  </div>
</template>


<script>
import TableOfContents from '@/components/TableOfContents.vue'

export default {
  components: {
    TableOfContents
  },
  async asyncData({ $content, params }) {
    const articles = await $content('neurips')
      .only(['title', 'description', 'img', 'slug', 'author'])
      .sortBy('createdAt', 'asc')
      .fetch()

    return {
      articles, searched:articles
    }
  },
  data () {
    return {
      query: '',
      searched: []
    }
  },
  watch: {
    async query (query) {
      if (!query) {
        this.searched = this.articles
        return
      }

      this.searched = await this.$content('neurips')
        .only(['title', 'slug'])
        .sortBy('createdAt', 'asc')
        .limit(12)
        .search(query)
        .fetch()
    }
  }
}
</script>
