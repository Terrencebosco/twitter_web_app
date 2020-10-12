from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    followers = db.Column(db.String(120), unique=True, nullable=False)
    # tweets are ordinal ids
    newest_tweet_id = db.Column(db.BigInteger, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(380), unique=True, nullable=False)
    embedding = db.Column(db.PickleType, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tweet', lazy=True))


    def __repr__(self):
        return '<tweet %r>' % self.tweet

# import from terminal

#flask shell: -> from twitoff.db_model import db, User, Tweet
# add user: -> u1 = User(username='terry', followers=10)
# commit: -> db.session.add(u1) -> db.seesion.commit()