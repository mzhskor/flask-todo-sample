from todo.database import db
from werkzeug.security import check_password_hash, generate_password_hash

class UserAlreadyExistsError(Exception):
    pass

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    @classmethod
    def register(cls, username, raw_password):
        return cls(username=username, password=generate_password_hash(raw_password))