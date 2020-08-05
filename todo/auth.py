from flask import (
    Blueprint, render_template, request, redirect, url_for, session
)
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from todo import login_manager
from todo.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('todo.index'))
        else:
            error = 'ユーザー名とパスワードの組み合わせが間違っています'

    return render_template('auth/login.html', error=error)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('todo.index'))