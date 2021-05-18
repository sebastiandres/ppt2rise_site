from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
from glob import glob
# See
# https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
# https://j2logo.com/tutorial-flask-leccion-4-login/

app.config['UPLOAD_PATH'] = 'pptx_files'
app.config['MAX_CONTENT_PATH'] = 1024*1024

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/pptx_files')
def pptx_files():
   pptx_files = {"name":"pptx files", "list":[]}
   pptx_files["list"] = glob("pptx_files/*.*")
   print(pptx_files)
   return render_template('pptx_files.html', files=pptx_files)

@app.route('/ipynb_files')
def ipynb_files():
   ipynb_files = {"name":"ipynb files", "list":[]}
   ipynb_files["list"] = glob("ipynb_files/*.*")
   print(ipynb_files)
   return render_template('ipynb_files.html', files=ipynb_files)

@app.route('/upload')
def upload():
   return render_template('upload.html')

@app.route('/uploaded', methods = ['GET', 'POST'])
def uploaded():
   if request.method == 'POST':
      f = request.files['file']
      filename = os.path.join(app.config['UPLOAD_PATH'] , secure_filename(f.filename) )
      f.save(filename)
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)