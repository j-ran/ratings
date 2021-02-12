"""This is to seed the movies database with some information."""

import os
import json #note that this is an import
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# access the movie info in our json file
# remember that "with" opens and closes the file 
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())


# Create movies, store them in list so we can use them
# to create fake ratings later
movies_saved_db = []
for movie in movie_data:
    # Get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    title, overview, poster_path = (movie['title'], movie['overview'], 
                                    movie['poster_path'])

    # this is day, month, year format as it is listed in our json file
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')                                

    # use a function from the crud file to make a Movie obj
    new_movie = crud.create_movie(title, overview, 
                                  release_date, 
                                  poster_path)
    
    # add Movie to list for the db
    movies_saved_db.append(new_movie)
    
## Can test this file now by running model.py and querying for something you know is in the json file
# Ex: 
# >> movie = Movie.query.filter(Movie.title == 'Ad Astra').first()
# >> movie.title
# Ad Astra    


## Create fake users using random numbers.
    
for n in range(10):
    # generate emails
    email = f'user{n}@test.com'
    password = 'test{n}'
    # generate usernames using the function from crud.py
    user = crud.create_user(email, password)

    # choose a movie for the entry
    for _ in range(10):
        random_movie = choice(movies_saved_db)
        # give the movie a random score between 1 and 5
        score = randint(1, 5)
        # use the create rating function from crud.py
        crud.create_rating(user, random_movie, score)

# can test again here:
# open model.py interactively
# >>> rating = Rating.query.first()
# will get a response 
# >>> rating.user
# will get the repr for user
# >>> rating.movie
# will get the repr for the first movie in the list
# that the user has rated
# >>> for user_rating in rating.user.ratings:
#     print(user_rating.score) 
# will get a list of ratings