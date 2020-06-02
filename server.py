"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect)

from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def homepage():
    pass
    return render_template('homepage.html')

@app.route('/all_movies')
def view_movies():
    movies = crud.all_movies()
    return render_template('all_movies.html', movies = movies)

@app.route('/all_movies/<movie_id>')
def movie_details(movie_id):
    movie = crud.get_movie_id(movie_id)
    return render_template('movie_details.html', movie = movie)

@app.route('/all_users')
def view_users():
    users = crud.all_users()
    return render_template('all_users.html', users=users)

@app.route('/all_users/<user_id>')
def user_info(user_id):
    user = crud.get_user_id(user_id)
    return render_template('user_info.html', user = user)






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
