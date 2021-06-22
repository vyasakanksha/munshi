<template>
  <div>
    <vue-editor v-model="content" :editor-toolbar="customToolbar" />
  </div>
</template>

<script>
import { VueEditor } from "vue3-editor";

export default {
  components: { VueEditor },

  data: () => ({
    content: "<p>Jam house</p>",
    customToolbar: [
      [{ header: [false, 1, 2, 3, 4] }],
      ["bold", "italic", "underline", "strike"],
      [{ list: "ordered" }, { list: "bullet" }],
      [
        { align: "" },
        { align: "center" },
        { align: "right" },
        { align: "justify" }
    ],
    ["blockquote"],
    [{ color: [] }, { background: [] }],
    ["clean"]
    ]
  })
};
</script>