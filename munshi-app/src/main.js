import App from './App.vue'
import * as Vue from 'vue'
import { store } from './store'
import Vuex from 'vuex'
import { createVuetify } from 'vuetify'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faMicrophone, faMicrophoneSlash } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faMicrophone, faMicrophoneSlash)

const app = Vue.createApp(App).component("font-awesome-icon", FontAwesomeIcon)

const vuetify = createVuetify({
  icons: {
    iconfont: 'fa',
  },
})

app.use(Vuex)
app.use(vuetify)
app.use(store)



app.mount('#app')




