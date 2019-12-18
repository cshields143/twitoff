'''Minimal flask app'''

from flask import Flask
from .models import DB

def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/chris/l/twitoff/TWITOFF/db.sqlite3'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  DB.init_app(app)

  @app.route('/')
  def root():
    return 'Welcome to Twitoff!'
    
  return app