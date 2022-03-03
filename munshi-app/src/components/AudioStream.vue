<template>
  <div id=recorder>
    <button @click="recordAudio()" type="button" id="button_record" class="btn btn-danger"> start
    </button>
    <button type="button" id="button_stop" class="btn btn-success" @click="stop"> stop
    </button>
    <button type="button" id="button_play" class="btn btn-success" @click="play"> play
    </button>
    <ul id="recordings"></ul>
    <div id="audio" class="audio" controls>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, defineComponent } from 'vue'


export default defineComponent({
    name: "AudioRecorder",
    data: () => {
        return {
            recorder: null,
            items: [],
            recordedVoice: [],
            mimeType: 'audio/webm'
        }
    },
    methods: {
        async recordAudio(){
            try {
                const stream = await navigator.mediaDevices.getUserMedia({
                    audio: true,
                    video: false
                });
                this.recorder = new MediaRecorder(stream, { mimeType: this.mimeType });
                this.recorder.start(1000);
                this.recorder.ondataavailable = (e) => {
                    this.items.push(e.data);
                }
                console.log("recorder started");
            } catch {
              console.log("permission error");
            }
        },
        stop(){
            // const self = this
            this.recorder.stop();
            console.log("recorder stopped");
            console.log(this.items);
        },
        play(){
            const list = document.getElementById('recordings');
            const recording = new Blob(this.items, {
                    type: this.mimeType
                });
            console.log(recording);
            const blobUrl = URL.createObjectURL(recording)
            console.log(blobUrl);
            const li = document.createElement('li');
            const audio = document.createElement('audio');
            const anchor = document.createElement('a');
            anchor.setAttribute('href', blobUrl);
            audio.setAttribute('src', blobUrl);
            audio.setAttribute('controls', 'controls');
            li.appendChild(audio);
            li.appendChild(anchor);
            list.appendChild(li);
        }
    }
})
</script>

<style scoped>

</style>