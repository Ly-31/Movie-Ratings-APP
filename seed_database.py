"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')
model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    datestring = movie['release_date']
    format = '%Y-%m-%d'
    date = datetime.strptime(datestring, format)
    db_movie = crud.create_movie(movie['title'],movie['overview'], date, movie['poster_path'])
    movies_in_db.append(db_movie)
model.db.session.add_all(movies_in_db)
model.db.session.commit()



for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(email, password)
    model.db.session.add(user)

    for i in range(10):
        score = randint(1,5)
        movie = choice(movies_in_db)
        rating = crud.create_rating(score, movie, user)
        model.db.session.add(rating)

model.db.session.commit()
