<template>
    <article>
        <MDHeader :text="article.title" h="1" add-hash></MDHeader>
        <p>{{ article.description }}</p>
        <p>Article last updated: {{ formatDate(article.updatedAt) }}</p>
        <TableOfContents :toc="article.$toc" />

        <nuxt-content :document="article" />
        <prev-next :prev="prev" :next="next" />
    </article>
</template>


<script>
import TableOfContents from '@/components/TableOfContents.vue'
import MDHeaderVue from '~/components/global/MDHeader.vue';
const createTree = function(list) {
    const path = [{ children: [] }];
    for (const obj of list) {
        path[obj.depth - 1].children.push(
            path[obj.depth] = { ...obj, children: [] }
        );
    }
    return path[0].children;
}

export default {
    components: {
        TableOfContents
    },
    async asyncData({ $content, params }) {
        const article = await $content('neurips', params.slug).fetch()
        const [prev, next] = await $content('neurips')
            .only(['title', 'slug'])
            .sortBy('createdAt', 'asc')
            .surround(params.slug)
            .fetch()

        return {
            article,
            prev,
            next
        }
    },
    methods: {
        formatDate(date) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' }
        return new Date(date).toLocaleDateString('en', options)
        }
    },
    computed: {
        toc() {
            return createTree([
                {depth:1, text:this.article.title} ,
                ...this.article.toc
            ])            
        }
    }
}
</script>
