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
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    # ratings = a list of Rating objects made 
    # through a backref in the Rating class

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


# Janaki, for herself, is going to write a class Movie in here ::
class Movie(db.Model):
    """A movie."""
    
    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    # ratings = a list of Rating objects made 
    # through a backref in the Rating class

    def __repr__(self):
        return f'<Movie movie_id={self.movie_id} title={self.title}>'


class Rating(db.Model):
    """A rating."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    score = db.Column(db.Integer)

    # relational method using backrefs
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    # create a relationship in the referenced Class to this table
    movie = db.relationship('Movie', backref='ratings')
    user = db.relationship('User', backref='ratings')

    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} score={self.score}>'


# The following is pretty much copy-paste
# Though for testing, you will want to change the postgresql database
# to a 'testdb' instead of 'db_uri'

    # Re: 'echo=True' in funciton args below ::
    # Set connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    # originally had the following line incorrect:
    # flask_app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql:///{db_uri}"
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    #in solution file, this says:
    # flask.app.config['SQLALCHEMY_ECHO'] = echo 
    flask_app.config['SQLALCHEMY_ECHO'] = True   
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app


    # this line works as is; does not need a db name passed in 
    # b/c that is done in the function definition (app line 70)
    connect_to_db(app)
