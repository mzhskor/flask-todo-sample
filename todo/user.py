from flask import (
    Blueprint, render_template, request, redirect, url_for
)

from todo.database import db
from todo.models.User import User, UserAlreadyExistsError
from todo.use_case.user import register_user

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        try:
            user = register_user(request.form['username'], request.form['password'])
            return redirect(url_for('todo.index'))
        except UserAlreadyExistsError as e:
            error = str(e)

    return render_template('user/register.html', error=error)
