import logging, json
from flask import current_app, Flask, render_template, request, jsonify, make_response
import crud, transcribe_async as transcribe

app = Flask(__name__)

bucket = "barricade_transcript"
project_name = "bar"

# Configure logging
if not app.testing:
 logging.basicConfig(level=logging.INFO)

# Add a root route. This is currently set to home.html
@app.route("/", methods=['GET', 'POST'])
def home():
   files = crud.blobs_list(bucket)
   audio_files = [x for x,y in files if y == '.wav']
   return render_template('home.html', audio_files=audio_files)

@app.route("/record", methods=['GET', 'POST'])
def record_audio():
   return render_template('record_audio.html')

@app.route("/upload", methods=['GET', 'POST'])
def upload_audio():
	files = crud.blobs_list(bucket)
	audio_files = [x for x,y in files if y == '.wav']

   # generate the name for the next audio file in series by incementing the number
	if audio_files:
		res1 = list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), audio_files))
		res2 = list(map(lambda sub:str(''.join([ele for ele in sub if not ele.isnumeric()])), audio_files))
		filename = "{}{}".format(res2[0], str(max(res1)+1))
	else:
		filename = "{}{}".format(project_name, 1)

	if request.method == 'POST':
		stat = request.files['data']
		stat.save("copy.wav")
		metadata = {'status': 0} # set status to new
		try:
			upload = crud.upload_blob(bucket, "copy.wav", stat.filename, metadata)
			return json.dumps({'status':'OK'})
		except Exception as e:
			return jsonify({'error' : e})
	return render_template('upload_audio.html', filename=filename)


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

