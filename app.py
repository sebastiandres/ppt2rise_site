from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# See
# https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
# https://j2logo.com/tutorial-flask-leccion-4-login/

app.config['UPLOAD_PATH'] = 'input_files'
app.config['MAX_CONTENT_PATH'] = 1024*1024

for k,v in app.config.items():
   print(k, v)

@app.route('/upload')
@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploaded', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      filename = os.path.join(app.config['UPLOAD_PATH'] , secure_filename(f.filename) )
      f.save(filename)
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)