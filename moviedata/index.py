import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    movies = json.load(open("movies.json", 'r'))
    return render_template('index/index.html', movies=movies)