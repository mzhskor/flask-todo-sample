from abc import ABC, abstractmethod
from enum import Enum
from todo.database import db

class TaskStatus(Enum):
    TODO = 1
    DOING = 2
    DONE = 3

class TaskId:
    def (self, id: str):
        self.id = id

class Task(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(30), unique=False, nullable=False)
    body = db.Column(db.String(120), unique=False, nullable=False)
    status = db.Column(db.Enum(TaskStatus), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    @classmethod
    def plan(cls, user_id, title, body):
        return cls(title=title, user_id=user_id, body=body, status=TaskStatus.TODO)

    def do(self):
        self.status = TaskStatus.DOING

    def complete(self):
        self.status = TaskStatus.DONE

    def is_owner(self, user_id):
        return self.user_id == user_id

class TaskRepository(ABC):
    @abstractmethod
    def save(entity: Task):
        pass

class SqlAlchemyTaskRepository(TaskRepository):
    def save(entity: Entity):
        db.session.add(entity)
        db.session.commit()
