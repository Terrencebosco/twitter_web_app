import numpy as np
from sklearn.linear_model import LogisticRegression
from .db_model import db, User
from .twitter import nlp, vectorize_tweet

def predict_user(user1, user2, tweet_text):
    user1 = User.query.filter(User.username == user1).one()
    user2 = User.query.filter(User.username == user2).one()

    user1_embeddings = np.array([tweet.embedding for tweet in user1.tweet])
    user2_embeddings = np.array([tweet.embedding for tweet in user2.tweet])

    #combine and create labels
    embeddings = np.vstack([user1_embeddings, user2_embeddings])

    y_labels = np.concatenate([np.ones(len(user1_embeddings)),
                               np.zeros(len(user2_embeddings))])

    # train model and convert input in to vecs
    model = LogisticRegression(max_iter=1000).fit(embeddings, y_labels)

    tweet_embedding = vectorize_tweet(nlp, tweet_text)

    return model.predict([tweet_embedding])[0]