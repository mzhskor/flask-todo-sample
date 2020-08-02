from flask import (
    Blueprint, render_template, request, redirect, url_for
)
from todo.database import db
from todo.models import Task, TaskStatus

bp = Blueprint('todo', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    todos = Task.query.filter_by(status=TaskStatus.TODO).all()
    doings = Task.query.filter_by(status=TaskStatus.DOING).all()
    dones = Task.query.filter_by(status=TaskStatus.DONE).all()
    return render_template('todo/index.html', todos=todos, doings=doings, dones=dones)

@bp.route('/', methods=['POST'])
def create():
    title = request.form['title']
    body = request.form['body']

    todo = Task.plan(title, body)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('todo.index'))

@bp.route('/do', methods=['POSt'])
def do():
    task_id = request.form['task_id']
    task = Task.query.get_or_404(task_id)
    task.do()
    db.session.commit()

    return redirect(url_for('todo.index'))

@bp.route('/complete', methods=['POSt'])
def complete():
    task_id = request.form['task_id']
    task = Task.query.get_or_404(task_id)
    task.complete()
    db.session.commit()

    return redirect(url_for('todo.index'))