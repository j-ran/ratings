""" Here we will put our CRUD functions – Create, Read, Update, Delete. """

from model import db, User, Movie, Rating, connect_to_db



# Functions start here!
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


# notes on release_date and how to format
# this is imported in model.py as 'from datetime import datetime'
# datetime.strptime(date_string, format)
# form of the string is "04-Feb-2021"
# form of the format is '%d-%b-%Y'; this is a "1989 C" standard 

def create_movie(title, overview, release_date, poster_path):
    "Create and return a new movie "

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)
    
    db.session.add(movie)
    db.session.commit()

    return movie



def create_rating(user, movie, score):
    "Create new rating taking a User and Movie."
    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)

