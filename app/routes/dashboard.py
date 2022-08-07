from flask import Blueprint, render_template

# this time, refix every route with "/dashboard"
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('') # /dashboard
def dash():
  return render_template('dashboard.html')

@bp.route('/edit/<id>') # /dashboard/edit/<id>
def edit(id):
  return render_template('edit-post.html')