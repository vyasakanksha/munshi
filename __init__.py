import logging, json
from flask import current_app, Flask, render_template, request
import crud, transcribe_async as transcribe

app = Flask(__name__)

bucket = "barricade_transcript"

# Configure logging
if not app.testing:
 logging.basicConfig(level=logging.INFO)

# Add a root route. This is currently set to home.html
@app.route("/", methods=['GET', 'POST'])
def home():
   files = crud.blobs_list(bucket)
   audio_files = [x for x,y in files if y == '.wav']
   return render_template('home.html', audio_files=audio_files)

@app.route("/edit/<filename>", methods=['GET', 'POST'])
def edit(filename):
   audio_filename = "{}.wav".format(filename)
   text_filename = "{}.json".format(filename)
   item = crud.blob_info(bucket, audio_filename)
   audio_url = "https://storage.cloud.google.com/{}/{}".format(bucket, audio_filename)
   text_url = "https://storage.cloud.google.com/{}/{}".format(bucket, text_filename)
   
   response = ""
   if crud.blob_exists(bucket, text_filename):
      item = crud.blob_info(bucket, text_filename)
      response = json.loads(item.download_as_string())

   if request.method == 'POST':
      if request.form['button'] == 'save':
         response = request.form['text']
         with open('copy.json', 'w', encoding='utf-8') as f:
            json.dump(response, f, ensure_ascii=False)
         crud.upload_blob(bucket, "copy.json", text_filename)
      if request.form['button'] == 'transcribe':
         transcript = transcribe.transcribe_gcs("gs://{}/{}".format(bucket, audio_filename))
         response = " ".join(transcript)
   return render_template('editor.html', url = audio_url, response = response)
      
if __name__ == "__main__":
	app.run()

