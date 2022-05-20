<template>
    <v-row>
        <MDHeader text="Results" h="1" add-hash/>
        <v-tabs v-model="tab">
            <v-tab 
                v-for="(tables, group, index) in groupedTables"
                :key="group" @change="tabTable=0"
            >
                {{group.replaceAll('_', ' ')}}
            </v-tab>
        </v-tabs>
        <v-tabs-items v-model="tab">
            <v-tab-item 
                v-for="(tables, group, index) in groupedTables"
                :key="`${group}-tab-item`"
            >   
                <nuxt-content :document="groupedArticles[group]"/>
                <v-tabs v-model="tabTable">
                    <v-tab 
                        v-for="(table, jndex) in tables"
                        :key="`${group}-tab-${table.name}-${table.id}`"
                    >
                        {{table.name.replaceAll('_', ' ')}}
                    </v-tab>
                </v-tabs>
                 <v-tabs-items v-model="tabTable">
                    <v-tab-item 
                       v-for="(table, jndex) in tables"
                        :key="`${group}-table-${table.name}-${table.id}`"
                    >   
                        <v-card
                            elevation="12"
                            class="pa-5 ma-5"
                            shaped keep-alive                    
                        >
                            <v-card-title>{{table.name}}</v-card-title>
                            <v-card-text>
                                <VRecordsTable        
                                    :ref="`${group}-table-${table.name}-${table.id}`" 
                                    :fieldOrder="table.headers.names"                        
                                    :json="table.results"    
                                    :fieldRenderFunctions="fieldRenderFunctions"        
                                    :fieldSynonymMap="fieldSynonymMap"        
                                />
                            </v-card-text>
                        </v-card>
                    </v-tab-item>
                </v-tabs-items>                
            </v-tab-item>
        </v-tabs-items>
        <v-col>
            <MDHeader text="Submit online today!" h="1" add-hash/>
            Click <a target="_blank" href="https://github.com/openproblems-bio/openproblems">here</a> to submit online via GitHub.
        </v-col>
    </v-row>
</template>

<script>
import _ from 'lodash'
import {VRecordsTable} from 'vfrxt'
import MDHeader from '~/components/global/MDHeader.vue'

const toFixed = (id, field, record, n=3) => record[field].toFixed(n)

const fieldRenderFunctions = {
    Code: (id, field, record) => {
        return `<a target="_blank" href="${record[field]}">${record.Version}</a>`
    },
    'Paper URL': (id, field, record) => {
        return `<a target="_blank" href="${record[field]}">paper</a>`
    },
    'Paper': (id, field, record) => {
        return `<a target="_blank" href="${record[field]}">${record.Paper}</a>`
    },
    'Runtime (min)': (id, field, record) => `${toFixed(id, field, record)} min`,
    'Micro F1 score': toFixed,
    'Memory (GB)': (id, field, record) => `${toFixed(id, field, record)} GB`,
    'F1 score': toFixed,
    'Accuracy': toFixed,
    'Mean squared error': toFixed,
    'kNN Area Under the Curve': toFixed
}
// set column names to something other than internal field name
export const fieldSynonymMap = {
  'Memory': 'Memory (GB)',
  'Runtime': 'Runtime (min)',
}


export default {
    components: {
    VRecordsTable,
    MDHeader
},
    data: () => ({
        tab: null,
        tabTable:null,
        fieldRenderFunctions, fieldSynonymMap,
        showTables: []
    }),
    async asyncData({ $content, params }) {
        const articles = await $content('results', {deep:true})
            .fetch()        
        return {
            articles, showTables: []
        }
    },
    methods: {
        setSort(str) {
            console.log(str, this.$refs[str])
            this.$refs[str].sortSpecifications.push(
                {field:'Rank', isAscending:true}
            )
        },
        getResultType(str) {
            const parts = str.split('/')
            return parts[parts.length - 1]
        },
        showTableAddDelete(index) {
            if (!this.showTables.includes(index)) {
                this.showTables.push(index)
            } else {

                let i = this.showTables.indexOf(index)
                this.showTables.splice(i, 1)
            }

        },
        throttleChange: _.throttle(function(event) {
            console.log(event)
            if (event === 3) {
                this.tabTable = event
            }
        }, 2000),
        test(event) {
            console.log(event)
            
        }
    },
    computed: {
        types() {
            return this.articles
                .filter(({extension}) => extension === '.md')
                .map(({dir}) => {
                    return this.getResultType(dir)
                })                
        },
        groupedTables() {
            let obj = {}
            this.types.forEach(_type => {
                obj[_type] = []
            });
            this.articles.forEach(article => {
                if (article.extension === '.md') return
                let _type = this.getResultType(article.dir)
                obj[_type].push(article)
            })
            return obj
        },
        groupedArticles() {
            let obj = {}
            this.types.forEach(_type => {
                obj[_type] = null
            });
            this.articles.forEach(article => {
                if (article.extension !== '.md') return
                let _type = this.getResultType(article.dir)
                obj[_type] = article
            })
            return obj
        }

    }
}
</script>