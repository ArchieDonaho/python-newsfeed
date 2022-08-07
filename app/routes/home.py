from flask import Blueprint, render_template

# Blueprint lets us consolidate routes onto a single bp object that the parent app can register later
# this corresponds to using the Router middleware of Express
bp = Blueprint('home', __name__, url_prefix='/')

# we add a "@bp.route()" before defining the function to turn it into a route
@bp.route('/')
def index():
  # return the rendered template instead of just a string
  return render_template('homepage.html')

@bp.route('/login') # /login
def login():
  return render_template('login.html')

# here we use a route parameter for the "id"
@bp.route('/post/<id>') # /post/<id>
def single(id):
  return render_template('single-post.html')