"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)


    return movie


def create_rating(score, movie, user):
    """Create and return a new rating."""
    rating = Rating(score=score, movie=movie, user=user)

    return rating


def get_movies():
    """return a list of all movie objects"""
    return Movie.query.all()


def get_movie_by_id(movie_id):
    movie = Movie.query.filter_by(movie_id = movie_id).one()
    return movie

def get_users():
    """return a list of all users objects"""
    return User.query.all()

def get_user_by_id(user_id):
    user = User.query.filter_by(user_id = user_id).one()
    return user

def get_user_by_email(email):

    return User.query.filter_by(email = email).one()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
