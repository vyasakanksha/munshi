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
        <v-icon v-if="isRecording">fas fa-microphone fa-2x</v-icon>
        <v-icon v-else>mdi-volume-high</v-icon>
        </v-btn>
      </div>
      <Recorder ref="myRecorder" />
    <Editor/>
  </div>
</template>

<script>
import Editor from './components/Editor.vue'
import Recorder from './components/Recorder.vue'


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
    Recorder
  },
  methods: {
    AudioRecorded() {
        this.isRecording = !this.isRecording;
        console.log("isRecording", this.isRecording)
        if(!this.isRecording) {
          console.log("Start Recoding")
        //   var device = navigator.mediaDevices.getUserMedia({ audio: true });
        //   device.then((stream) => {
        //     // console.log(stream)
        //     // use this!
        //     this.recorder = new MediaRecorder(stream);
        //     this.recorder.ondataavailable = (e) => {
        //         console.log(e)
        //         if (this.recorder.state == "inactive") {
        //           var blob = new Blob(this.items, { type: "audio/*" });
        //           var audio = document.getElementById("audio");
        //           var mainaudio = document.createElement("audio");
        //           mainaudio.setAttribute("controls", "controls");
        //           audio.appendChild(mainaudio);
        //           mainaudio.innerHTML =
        //               '<source src="' +
        //               URL.createObjectURL(blob) +
        //               '" type="audio/*" />';
        //       }
        //     };
        //     this.recorder.start();
        //   });
        } else if(this.isRecording) {
          console.log("Stop Recoding")
        //   this.recorder.stop();
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
