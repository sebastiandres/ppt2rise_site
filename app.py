from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
from pptx_to_RISE import ppt2rise
import shutil
from glob import glob
from datetime import datetime

# See
# https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
# https://j2logo.com/tutorial-flask-leccion-4-login/
app = Flask(__name__)

app.config['PPTX_PATH'] = 'files/pptx_files/'
app.config['IPYNB_PATH'] = 'files/ipynb_files/'
app.config['ZIP_PATH'] = 'files/zip_files/'
app.config['ALLOWED_EXTENSIONS'] = ['ipynb',]  # Not used
app.config['MAX_CONTENT_PATH'] = 1024*1024 # Not used

def make_archive(source, destination):
   base = os.path.basename(destination)
   name = base.split('.')[0]
   format = base.split('.')[1]
   archive_from = os.path.dirname(source)
   archive_to = os.path.basename(source.strip(os.sep))
   print(source, destination, archive_from, archive_to)
   shutil.make_archive(name, format, archive_from, archive_to)
   shutil.move('%s.%s'%(name,format), destination)

@app.route('/', methods = ['GET', 'POST'])
def index():
   f = request.files['file']
   filename = secure_filename(f.filename)
   print(f"filename: {filename}")
   if request.method == 'POST' and filename[-5:]==".pptx":
      # Get the file properties
      basename = filename.replace(".pptx", "")
      # Timestamp to dynamic path
      timestamp_str = datetime.now().strftime("%Y-%b-%d-%H-%M-%S")
      # Main path
      global_path = os.getcwd()
      # Print the paths
      print(f"basename: {basename}")
      print(f"global_path: {global_path}")
      # pptx files and paths
      pptx_filename = filename
      pptx_basepath = os.path.join(global_path, app.config['PPTX_PATH'])
      pptx_filepath = os.path.join(pptx_basepath, pptx_filename)
      print("pptx_filepath", pptx_filepath)
      # ipynb files and paths
      ipynb_filename = basename + ".ipynb"
      ipynb_basepath = os.path.join(global_path, app.config['IPYNB_PATH'] , basename + timestamp_str)
      ipynb_filepath = os.path.join(ipynb_basepath, ipynb_filename)
      print("ipynb_filepath", ipynb_filepath)
      # zip files and paths
      zip_filename = basename + timestamp_str + ".zip"
      zip_basepath = os.path.join(global_path, app.config['ZIP_PATH'])
      zip_filepath = os.path.join(zip_basepath , zip_filename)
      print("zip_filepath", zip_filepath)
      try:
         print("Creating ipynb directory.")
         os.mkdir(ipynb_path)
      except:
         pass
      # Store in folder
      f.save(pptx_filepath)
      # Convert
      ppt2rise.ppt2rise(pptx_filepath, ipynb_filepath)  
      # Zip
      make_archive(ipynb_basepath, zip_filepath)
      # Offer to download it
      return send_from_directory(zip_basepath, zip_filename, as_attachment=True)
   else:
      return render_template('index.html')

@app.route('/faq')
def faq():
      return render_template('faq.html')

		
if __name__ == '__main__':
   app.run(debug = True)