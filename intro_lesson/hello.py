'''Minimal flask app'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return 'hello, world'

@app.route('/about')
def showit():
  return render_template('about.html')