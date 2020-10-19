from todo import db
from todo.domain.task import Task, TaskRepository

class SqlalchemyTaskRepository(TaskRepository):
    def save(task: Task):
        db.add(task)
        db.commit()