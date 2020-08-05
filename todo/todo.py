from flask import (
    Blueprint, render_template, request, redirect, url_for, session, abort
)
from flask_login import login_required, current_user
from todo.database import db
from todo.models import Task, TaskStatus

bp = Blueprint('todo', __name__, url_prefix='/')

def check_owner(task: Task, user_id: int):
    if not task.is_owner(user_id):
        abort(403)

@bp.route('/', methods=['GET'])
@login_required
def index():
    todos = Task.query.filter_by(user_id=current_user.id, status=TaskStatus.TODO).all()
    doings = Task.query.filter_by(user_id=current_user.id, status=TaskStatus.DOING).all()
    dones = Task.query.filter_by(user_id=current_user.id, status=TaskStatus.DONE).all()
    return render_template('todo/index.html', todos=todos, doings=doings, dones=dones)

@bp.route('/', methods=['POST'])
@login_required
def create():
    title = request.form['title']
    body = request.form['body']

    todo = Task.plan(current_user.id, title, body)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('todo.index'))

@bp.route('/do', methods=['POST'])
@login_required
def do():
    task_id = request.form['task_id']
    task = Task.query.get_or_404(task_id)
    check_owner(task, current_user.id)
    task.do()
    db.session.commit()

    return redirect(url_for('todo.index'))

@bp.route('/complete', methods=['POST'])
@login_required
def complete():
    task_id = request.form['task_id']
    task = Task.query.get_or_404(task_id)
    check_owner(task, current_user.id)
    task.complete()
    db.session.commit()

    return redirect(url_for('todo.index'))

@bp.route('/show/<int:task_id>')
@login_required
def show(task_id: int):
    task = Task.query.get(task_id)
    check_owner(task, current_user.id)
    return render_template('todo/show.html', task=task)