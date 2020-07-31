from flask import (
    Blueprint, render_template, request
)

from todo.database import db
from todo.models import User

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()

    return render_template('user/register.html')
