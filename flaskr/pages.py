from flask import (
    Blueprint, flash, g, redirect, render_template, session, request, url_for
)
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openai
import nltk
import openai
from googlesearch import search
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('pages', __name__)

def create_app():
    app = ...
    # existing code omitted

    from . import pages
    app.register_blueprint(pages.bp)
    app.add_url_rule('/', endpoint='index')

    return app

@bp.route('/', methods =['GET', 'POST'])
def index():
    return render_template('pages/index.html')#, posts=posts)

@bp.route('/home', methods =['GET', 'POST'])
def home():
    db = get_db()
    user_id = session.get('user_id')

    posts = db.execute(
        'SELECT name,profession,age, programs FROM kids WHERE user_id = ?', (user_id,)
    ).fetchall()
    
    
    return render_template('pages/home.html', posts=posts)



