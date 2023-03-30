"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
from flask import Flask
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/movies')
def moviespage():
    movies = crud.get_movies()
    return render_template('movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def movie_detail(movie_id):
    movie_details = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie_details)


@app.route('/users')
def users_page():
    users = crud.get_users()
    return render_template('users.html', users=users)

@app.route('/users/<user_id>')
def user_detail(user_id):
    user_details = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user_details)



@app.route('/users', method=["POST"])
def register_user():
    """Create a new user"""
    email = request.form.get('email')
    print(email)

    return 'hello'



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
