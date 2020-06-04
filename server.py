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
    # print(session["user_id"],"!!!")
    
    # session["user_id"] == None

    return render_template('homepage.html')

@app.route('/all_movies')
def view_movies():
    movies = crud.all_movies()
    return render_template('all_movies.html', movies = movies)

@app.route('/all_movies/<movie_id>')
def movie_details(movie_id):
    movie = crud.get_movie_id(movie_id)
    return render_template('movie_details.html', movie = movie)

@app.route('/users', methods = ["POST"])
def register_user():
    # print(session["user_id"], "register")
    email =  request.form.get("email")
    password = request.form.get("password")
    print(email,"email*********")

    user = crud.get_user_email(email)
    print(user, "user********")

    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return redirect('/')

@app.route('/handle-login', methods=['POST'])
def handle_login():
    """Log user into application."""

    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_email(email)
    print(user,"user***********")

    if user:

        if user.password == password and user.email == email:
            session['user_id'] = user.user_id
            print(session['user_id'], "session*********")
            flash(f'Logged in as {email}')
        else:
            flash('Wrong email or password!')
    else:
        
        flash("email doesn't exist")
    return redirect ('/')
            

     

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
