import json
from statistics.statistics import average

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    movies = json.load(open("movies.json", 'r'))
    return render_template('index/index.html', movies=movies)

@bp.route('/statistics')
def statistics():
    movies = json.load(open("movies.json", 'r'))
    # 3.2 - Qual o tempo de duracao medio dos filmes obtidos?
    movie_duration = [int(movies[movie][6]) for movie in movies.keys() if movies[movie][6] != '\\N']
    average_time = average(movie_duration)
    return render_template('index/statistics.html', average_time=average_time, movie_duration = movie_duration)