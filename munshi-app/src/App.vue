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
    AudioRecorded() {
      if(this.isRecording) {
        this.stopRecord()
      } else {
        this.startRecord()
      }
    },
    async startRecord() {
      var device = navigator.mediaDevices.getUserMedia({audio: true})
      
      device.then((stream) => {
        this.recorder = new RecordRTCPromisesHandler(stream, {
          mimeType: 'audio/webm'
        }),
        this.recorder.startRecording();
        this.recorder.stream = stream
        this.isRecording = true;
        console.log(this)
        console.log("Start Recoding")
      })
      .catch(function(error) {
        alert("Unable to capture your audio device. Please check console logs.");
        console.error(error);
      });
    },
    async stopRecord() {
      console.log("Stop Recoding")
      await this.recorder.stopRecording()
      let blob = await this.recorder.getBlob();
      let url = URL.createObjectURL(blob);
      this.isRecording = false;
      console.log(url)
      // window.open(url) test that the reording works!!


      this.recorder.destroy()
      this.recorder.stream.getTracks().forEach(track => track.stop())
      this.recorder = null;
    },
  },
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
