"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# our code here
class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)

    # ratings = a list of Rating objects made through backrefs
    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Movie(db.Model):
    """A movie."""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)
    
    # ratings = a list of Rating objects – made through backref

    def __repr__(self):
        return f'<Movie movie_id={self.movie_id} title={self.title}>'

class Rating(db.Model):
    """Ratings for movies."""
    __tablename__ = "ratings"
    
    rating_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    # we peg this table to the other tables with these variables
    movie = db.relationship('Movie', backref='ratings')
    user = db.relationship('User', backref='ratings')

    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} score={self.score}>'

def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    # originally had the following line incorrect:
    # flask_app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql:///{db_uri}"
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = True    
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    # this line works as is; does not need a db name passed in 
    # b/c that is done on lines 67-68
    connect_to_db(app)
