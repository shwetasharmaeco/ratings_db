import os
import json
import crud
import model
import server
from random import choice, randint
from datetime import datetime 

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as file:
    movies_data = json.loads (file.read())
    print(movies_data)

movies_list = []



for movie in movies_data:
    date_str = movie['release_date']
    format = "%Y-%m-%d"
    date = datetime.strptime(date_str, format)

    add_movie = crud.create_movie (movie['title'], movie['overview'], date, movie['poster_path'])
    movies_list.append(add_movie)
print(movies_list)

for n in range(10):
    email = f'{n}@testmail.com'
    password = 'ghjk'
    user = crud.create_user(email,password)
    
    for i in range(10):
        random_movie = choice(movies_list)
        score = randint(1,5)
        crud.create_rating(score, random_movie, user)
