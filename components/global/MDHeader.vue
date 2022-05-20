<template>
  <v-hover v-slot:default="{ hover }" :id="slugText">
    <div class="">
      <div class="d-inline-flex" @click="hash">
        <div :class="cls">
          {{text}}
        </div>
        <v-icon v-if="addHash" :small="h>=6" :style="`opacity:${hover?1:0}`">mdi-pound</v-icon>
      </div>
    </div>
  </v-hover>
</template>

<script>
// const vuetifyClasses = {
//   1: 'text-h1',
//   2: 'text-h2',
//   3: 'text-h3',
//   4: 'text-h4',
//   5: 'text-h5',
//   6: 'text-h6',
//   7: 'subtitle-1',
//   8: 'subtitle-2',
//   9: 'body-1',
//   10: 'body-2',
//   11: 'caption',
//   12: 'overline',
// }

const vuetifyClasses = {
  1: 'text-h3',
  2: 'text-h4',
  3: 'text-h5',
  4: 'text-h6',
  5: 'subtitle-1',
  6: 'subtitle-2',
  7: 'body-1',
  8: 'body-2',
  9: 'caption',
  10: 'overline',
}

import slugify from 'slugify'
const slugSettings = {
  replacement: '-',
  remove: /[*+~.()'"!:@]/g,
  lower: true,
  strict:true,
  locale: 'en'
}

export default {
  name: 'MDHeader',
  props: {
    text: { type:String },
    h: { type:[Number, String] },
    addHash: { type:Boolean, default:false },
    alternate: {type:String}
  },
  computed: {
    slugText() {
      let text = this.alternate ? this.alternate : this.text
      return slugify(text, slugSettings)
    },
    slug() {
      return `#${this.slugText}`
    },
    cls() {
      return vuetifyClasses[this.h]
    }
  },
  methods : {
    hash() {
      if (this.addHash) {
        // this.$router.push(this.$route.path+this.slug)
      }
      this.$vuetify.goTo(this.slug)
      this.$emit('hash', this.slug)
    }
  }

}
</script>

<style>
</style>
