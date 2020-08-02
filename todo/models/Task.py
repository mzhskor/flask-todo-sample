from enum import Enum
from todo.database import db

class TaskStatus(Enum):
    TODO = 1
    DOING = 2
    DONE = 3

class Task(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(30), unique=False, nullable=False)
    body = db.Column(db.String(120), unique=False, nullable=False)
    status = db.Column(db.Enum(TaskStatus), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    @classmethod
    def plan(cls, title, body):
        return cls(title=title, body=body, status=TaskStatus.TODO)

    def do(self):
        self.status = TaskStatus.DOING

    def complete(self):
        self.status = TaskStatus.DONE