<template>
  <div>
    <template v-if="children">
      <template v-if="root">
        <TableOfContentsItem
          v-for="child in children"
          :children="child.children"
          :icon="child.icon"
          :to="child.to"
          :text="child.text"
          :root="false"
          :key="child.id"
          :subgroup='false'
        />
      </template>
      <template v-else>
        <v-list-group
          ref="group"
          class=""
          :prepend-icon="icon"
          :group="text"
          :sub-group="subgroup"
          :value="true"
          @click.stop="tocMove"
          :active-class="'not-active'"
        >
          <template v-slot:activator @click.stop="tocMove">
            <v-list-item-title>
              <a :href="to" class="scrollactive-item">{{text}}</a>
            </v-list-item-title>
          </template>
          <v-list-item-group
            v-if="children"
            :value="true"
            class=""
            :active-class="'not-active'"
          >
            <TableOfContentsItem
              v-for="child in children"
              :children="child.children"
              :icon="child.icon"
              :to="child.to"
              :text="child.text"
              :root="false"
              :key="child.id"
              :subgroup="true"
            />
          </v-list-item-group>
        </v-list-group>
      </template>
    </template>
    <template v-else>
      <v-list-item
        link @click.stop="tocMove"
        :active-class="'not-active'"
        :input-value="true"
      >
        <v-list-item-icon>
          <v-icon
           v-text="icon"
           :opacity="icon?1:0"
          >
          </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title >
            <a :href="to" class="scrollactive-item">{{text}}</a>
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </template>

  </div>
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


export default {
  name: 'TableOfContentsItem',
  props: [
    'icon',
    'to',
    'text',
    'children',
    'root',
    'subgroup'
  ],
  data: () => ({
    childrenState: {

    }
  }),
  methods: {
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
}
</script>

<style media="screen" scoped>
a.scrollactive-item.toc-active {
  color: #1976D2 !important;
  text-decoration:underline !important;
}

a.scrollactive-item {
  color: rgba(0, 0, 0, 0.87) !important;
  text-decoration: none; /* no underline */
}

</style>
