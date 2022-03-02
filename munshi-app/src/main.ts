import { createApp } from 'vue'
import App from './App.vue'
import store from './store'

import '@vueup/vue-quill/dist/vue-quill.snow.css';
import '@vueup/vue-quill/dist/vue-quill.bubble.css';

createApp(App).use(store).mount('#app')

