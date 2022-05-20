<template>
  <nuxt-content :document="md"/>
</template>

<script>
export default {
  name: 'IndexPage',
  async asyncData({ $content, params }) {
    const articles = await $content('home')
      .sortBy('createdAt', 'asc')
      .limit(1)
      .fetch()

    return {
      md: articles[0]
    }
  },
}
</script>
