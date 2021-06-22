<template>
  <div id="app">
      <div>
        <v-btn
          icon
          color="#808080"
          @click="AudioRecorded"
        >
        <!-- <v-icon v-if="isRecording"><i class='fa fa-microphone fa-2x'></i></v-icon>
        <v-icon v-else><i class='fa fa-microphone-slash fa-2x'></i></v-icon> -->
        <v-icon v-if="isRecording"><font-awesome-icon icon="microphone" /></v-icon>
        <v-icon v-else><font-awesome-icon icon="microphone-slash" /></v-icon>
        </v-btn>
      </div>
    <Editor/>
  </div>
</template>

<script>
import Editor from './components/Editor.vue'
import { RecordRTCPromisesHandler } from "recordrtc";


export default {
  name: 'App',
  data () {
    return {
      isRecording: false,
      recorder: null,
      items: null

    }
  },
  components: {
    Editor,
  },
  methods: {
    async AudioRecorded() {
        if(!this.isRecording) {
          console.log("Start Recoding")
          let stream = await navigator.mediaDevices.getUserMedia({video: true, audio: true});
          var recorder = new RecordRTCPromisesHandler(stream, {
              type: 'video'
          });
          recorder.startRecording();
          this.isRecording = false;
          
        } else if(this.isRecording) {
          this.isRecording = false;
          console.log("isRecording", this.isRecording)

          await recorder.stopRecording();
          // let blob = await recorder.getBlob();
        }
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
