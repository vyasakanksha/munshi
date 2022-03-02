<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <QuillEditor />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import QuillEditor from './components/MainEditor.vue';

export default defineComponent({
  name: 'App',
  components: {
    QuillEditor
  }
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  height: 100vh;
}
</style>
