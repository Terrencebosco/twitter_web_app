from flask import Flask, render_template, request
from .db_model import db, User, Tweet
from .twitter import add_user_tweepy

def create_app():
    "create an instance of our app"

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///twitoff.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app) #link sql to flask app

    @app.route('/')
    def root():
        return render_template('base.html', title='Home', users=User.query.all())

    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def add_or_update_user(name=None, message=''):
        name = name or request.values['user_name']

        try:
            if request.method == "POST":
                add_user_tweepy(name)
                message = "User {} successfully added!".format(name)
            tweets = User.query.filter(User.username == name).one().tweet
        except Exception as e:
            print(f'Error adding {name}: {e}')
            tweets = []

        return render_template('user.html', title=name, tweets=tweets, message=message)

    return app