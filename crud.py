""" here we will put our CRUD functions"""
from model import db, User, Movie, Rating, connect_to_db
import datetime

# Functions start here!
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, poster_path, release_date):
    "Create and return a new movie "

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)
    print("movie", movie)
    db.session.add(movie)
    db.session.commit()

    print(movie)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)

