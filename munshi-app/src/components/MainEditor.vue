<template>
  <div id=editor>
    <h1> {{ contentHeading }}</h1>
    <QuillEditor 
    theme="snow"
    :toolbar="toolbarOptions"
    v-model="contentDelta" contentType="delta" />
  </div>
</template>

<script lang="ts">
import { ref, defineComponent } from 'vue'
import { QuillEditor, Delta } from '@vueup/vue-quill'
export default defineComponent({
  components: {
    QuillEditor,
  },
  setup: () => {
    const contentDelta = ref<Delta>(
      new Delta([
        { insert: 'Gandalf', attributes: { bold: true } },
        { insert: ' the ' },
        { insert: 'Grey', attributes: { color: '#ccc' } },
      ])
    )
    const contentHeading = ref('Tuffy the Turtle')
    var toolbarOptions = [
      ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
      ['blockquote'],

      [{ 'direction': 'rtl' }],                         // text direction

      [{ 'header': [1, 2, 3, 4, 5, 6, false] }],

      [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
      [{ 'align': [] }],

      ['clean']                                         // remove formatting button
    ];
    return { contentDelta, contentHeading, toolbarOptions}
  },
})
</script>

<style scoped>
#editor {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  height: 60vh;
}
</style>