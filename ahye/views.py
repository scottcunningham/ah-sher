import os

from flask import request, send_from_directory, url_for

from ahye import app
from ahye.flaskext.mako import render_template as render
from ahye.lib import generate_filename
from ahye.settings import VDIR, LOCAL_UPLOADS_DIR


@app.route('/', methods=['GET'])
def home():
    return render('/home.mako')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.files['imagedata']
    filename = generate_filename()
    data.save(os.path.join(LOCAL_UPLOADS_DIR, filename))
    return url_for('serve_upload', filename=filename, _external=True)


@app.route('/%s/<filename>' % VDIR)
def serve_upload(filename):
    return send_from_directory(LOCAL_UPLOADS_DIR, filename)


@app.route('/favicon.ico')
def serve_favicon():
    return send_from_directory(os.path.join(LOCAL_UPLOADS_DIR, '..'), 'favicon.ico')
