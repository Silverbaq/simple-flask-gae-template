from app import app
from flask import render_template


@app.route('/')
def index():
    text = 'Hello World!'
    return render_template('index.html', hello=text)
