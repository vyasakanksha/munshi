import logging, json, datetime, re
from itertools import groupby, chain
from flask import current_app, Flask, render_template, request, jsonify, make_response
import crud, transcribe_async as transcribe

app = Flask(__name__)

bucket = "barricade_transcript"
project_name = "barricade"

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


@app.route("/record", methods=['GET', 'POST'])
def record_audio():
   return render_template('record_audio.html')


@app.route("/upload", methods=['GET', 'POST'])
def upload_audio():
   files = crud.blobs_list(bucket)
   audio_files = [x for x,y in files if y == '.wav']
   grouped = [groupby(x, str.isdigit) for x in audio_files]

   # generate the name for the next audio file in series by incementing the number
   if audio_files:
      filenumber = get_filenumber(audio_files)

      filename_temp = ''.join(chain.from_iterable("{}" if k else g for k,g in grouped[0]))

      filename = filename_temp.format(max(filenumber)+1, datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
   else:
      filename = "{}{}_{}".format(project_name, 1, datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

   if request.method == 'POST':
      stat = request.files['data']
      stat1 = request.form['filename']
      stat.save("copy.wav")
      metadata = {'status': 0} # set status to new
      try:
         upload = crud.upload_blob(bucket, "copy.wav", stat.filename, metadata)
         return json.dumps({'status':'OK'})
      except Exception as e:
         return jsonify({'error' : e})
   return render_template('upload_audio.html', filename=filename)


def get_filenumber(audio_files):
   # generate the name for the next audio file in series by incementing the number
   num_lst = []

   if audio_files:
      grouped = [groupby(x, str.isdigit) for x in audio_files]

      for group in grouped:
         tmp_lst = []
         for key, grp in group:
            if key:
               tmp_lst.append("".join(list(grp)))
         num_lst.append(int(tmp_lst[0]))
   return num_lst

      
if __name__ == "__main__":
	app.run()

