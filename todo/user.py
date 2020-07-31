from flask import (
    Blueprint
)

from todo.database import db

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/register', method='GET')
def register():
    return render_template('user/register.html')