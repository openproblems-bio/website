import colors from 'vuetify/es5/util/colors'


const gitlabPagesRepositorySlug = 'website'
const isGitlabPages  = (process.env.DEPLOY_ENV === 'GITLAB_PAGES' )
const isNetlify = (process.env.DEPLOY_ENV === 'NETLIFY' )
const staticLoc = isGitlabPages 
  ? `/${gitlabPagesRepositorySlug}/`
  : `/`



export default {
  vue: {
    config: {
      productionTip: true,
      devtools: (!isGitlabPages && !isNetlify)
    }
  },


  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s',
    title: 'Open Problems',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/icon.png' }
    ],
    // ADDED FOR MATHJAX
    script: [
      {
        src: 'https://polyfill.io/v3/polyfill.min.js?features=es6',
        async: true,
        defer: true
      },
      {
        // src: 'https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js',
        src: 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js',
        async: true,
        defer: true,
        id:"MathJax-script"
      },
    ],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
  ],

  

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    {
      src: '@/plugins/scrollactive.js',
      ssr: true
    },
    {
      src: '@/plugins/youtube.js',
      ssr: false
    },
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/typescript
    '@nuxt/typescript-build',
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    // https://go.nuxtjs.dev/content
    '@nuxt/content',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: '/',
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en'
    }
  },

  // Content module configuration: https://go.nuxtjs.dev/config-content
  content: {
    markdown: {
      prism: {
        theme: 'prism-themes/themes/prism-material-oceanic.css'
      }
    }
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        light: {
          primary: colors.blueGrey.base,
          secondary: colors.red.base,
          accent: colors.indigo.base,
          error: colors.pink.base,
          warning: colors.deepOrange.base,
          info: colors.teal.base,
          success: colors.green.base
        },
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },

  generate: {
    dir: 'public',
    fallback: true
  },
  /*
  ** Customize the base url
  */
  router: {
    base: staticLoc, //this is whatever the project is named
  },


  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
