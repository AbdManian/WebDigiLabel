from flask import render_template, request
from app import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    info = dict(title='DigiLabel')
    files = request.files.getlist("file")
    for file in files:
        print("Content: ", file.filename)
    return render_template('index.html', **info)
