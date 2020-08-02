from todo.database import db
from todo.models.User import User, UserAlreadyExistsError

def register_user(username, raw_password):
    if db.session.query(User.id).filter_by(username=username).scalar() is not None:
        raise UserAlreadyExistsError(f'username "{username}" is already used.')

    user = User.register(username, raw_password)
    db.session.add(user)
    db.session.commit()
    return user
