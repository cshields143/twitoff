from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
  '''Twitter users that we analyze'''
  id = DB.Column(DB.BigInteger, primary_key=True)
  name = DB.Column(DB.String(15), nullable=False)
  def __repr__(self):
    return f'<User {self.name}>'

class Tweet(DB.Model):
  '''Tweets that we pull'''
  id = DB.Column(DB.BigInteger, primary_key=True)
  text = DB.Column(DB.Unicode(300))
  user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
  user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
  embedding = DB.Column(DB.PickleType, nullable=False)
  def __repr__(self):
    return f'<Tweet {self.text}>'