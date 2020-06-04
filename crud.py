""" CRUD operations """

from model import db, User, Movie, Rating, connect_to_db

def create_user(email,password):
    """ create  and return user if doesn't already exists in database """

    user =  User (email = email, password = password)
    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """ creates and returns a movie object """

    movie = Movie(title = title, overview = overview, release_date = release_date, poster_path= poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def create_rating(score, movie, user):
    """ create and return rating """

    rating = Rating(score = score, movie = movie, user = user)

    db.session.add(rating)
    db.session.commit()

    return rating

def all_movies():
    return Movie.query.all()

def get_movie_id(movie_id):
    return Movie.query.get(movie_id)

def all_users():
    return User.query.all()

def get_user_id(user_id):
    return User.query.get(user_id)

def get_user_email(email):
    return User.query.filter(User.email == email).first()
 

if __name__ == '__main__':
    from server import app
    connect_to_db(app)