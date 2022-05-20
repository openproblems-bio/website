<template>
  <v-navigation-drawer
    class="toc-drawer"
    clipped app    
    :disable-route-watcher="true"
    width="300px"
  >
  <v-treeview 
   :items="toc" dense hoverable open-all 
   :item-text="'text'" color="accent" open-on-click shaped

  >
    <template v-slot:label="{ item, open }">
      <scrollactive
        @click.stop="tocMove"
        @update:active="tocMove"
        active-class="toc-active"
        :offset="100"
        class="my-nav" v-on:itemchanged="onItemChanged"
      >
        <a :href="item.to" class="scrollactive-item">{{item.text}}</a>
      </scrollactive>

    </template>
  </v-treeview>
</v-navigation-drawer>
  <!-- <v-navigation-drawer
    class="toc-drawer"
    clipped app
    :mobile-breakpoint="'900'"
    :disable-route-watcher="true"
    width="300px"
  >
    <scrollactive
      active-class="toc-active"
      :offset="100"
      class="my-nav" v-on:itemchanged="onItemChanged"
    >
      <v-list dense nav shaped class="px-0 mx-0">
        <v-subheader class="secondary--text title"
          style="background-color:white;z-index:1000;position:sticky; top:0px;"
        >
          Contents
        </v-subheader>
        <TableOfContentsItem class="" :children="toc" :root="true"/>
      </v-list>
    </scrollactive>
  </v-navigation-drawer> -->
</template>

<script>
import slugify from 'slugify'
const slugSettings = {
  replacement: '-',
  remove: /[*+~.()'"!:@]/g,
  lower: true,
  strict:true,
  locale: 'en'
}

import TableOfContentsItem from '@/components/TableOfContentsItem.vue'


const traverse = function(tree, current, fn) {
    //process current node here

    //visit children of current
    for (let i = 0; i < current.length; i++) {
      let node = current[i]

      fn(node)

      let children = node.children
      if (children) {
        traverse(tree, children, fn)
      }
    }
}


export default {
  name: 'TableOfContents',
  components: {
    TableOfContentsItem,
  },
  props: [
    'toc'
  ],
  data: () => ({

  }),
  computed: {
    
  },
  methods: {
    onItemChanged(event, currentItem, lastActiveItem) {
      // console.log(event, currentItem, lastActiveItem)
    },
    tocMove(event) {
      const slug = slugify(this.text, slugSettings)
      const here = this.$route.path
      const there = `${here}${slug}`
      try {
        if (this.to === undefined) {
          this.$vuetify.goTo(`#${slug}`)
        } else {
          this.$vuetify.goTo(this.to)
        }
      } catch (e) {

      }
    }
  },
  mounted() {
    let that = this
    let hash = this.$route.hash
    traverse(this.toc, this.toc, (node)=>{
      // node.name = node.text
      if (node.to === undefined) {
        node.to = `#${slugify(node.text, slugSettings)}`
      }
      if (node.to === hash) {
        try {          
          that.$vuetify.goTo(node.to)
        } catch (e) {

        } finally {

        }
      }
    })
  }
}
</script>
<style>
  .toc-wrapper {
    /* position:relative !important;
    grid-column-start: 1;
    grid-row-start: 1 ;
    grid-column-end: 3;
    grid-row-end: 3;
    position: sticky!important;
    top: 0px!important;
    padding-right: 10px!important; */
    width:100%;
  }

  /* .v-navigation-drawer__content, .my-nav, .v-list {
    position: sticky!important;
    top: 0px!important;
  }
  .v-list-item__icon:first-child {
    margin-right: 0px !important;
  }
  .v-list-item__icon {
    min-width: 12px !important;
  }
  .v-list-group--sub-group .v-list-group__header {
    padding-left: 12px !important;
  }
  .v-list-group--sub-group .v-list-group__items .v-list-item {
    padding-left: 24px !important;

  } */

a.scrollactive-item.toc-active {
  color: #1976D2 !important;
  text-decoration:underline !important;
}

a.scrollactive-item {
  color: rgba(0, 0, 0, 0.87) !important;
  text-decoration: none; /* no underline */
}

.v-treeview-node__level {
  width: 10px!important;
}
.v-treeview-node__root {
  margin-top: 0px!important;
  margin-bottom: 0px!important;
  /* padding-left: 0px!important; */
}
</style>
