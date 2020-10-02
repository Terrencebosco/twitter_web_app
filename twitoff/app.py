from flask import Flask
from .db_model import db, User, Tweet

def create_app():
    "create an instance of our app"

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///twitoff.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app) #link sql to flask app

    @app.route('/')
    def root():
        return "welcome to twitoff"
    
    @app.route('/user/<username>/<followers>')
    def add_user(username, followers):
        user = User(username=username, followers=followers)
        db.session.add(user)
        db.session.commit()
        return (f'{username} has been added.')
    
    @app.route('/tweet/<text>/<user>')
    def add_tweet(user, text): 
        print('tweet')
        t = Tweet(user=user, text=text)
        db.session.add(t)
        db.session.commit()
        return (f'{text} has been added.')

    return app