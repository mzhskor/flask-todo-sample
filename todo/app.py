from flask import Flask, url_for, render_template, abort
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page!!!'


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/user/<username>')
def user(username):
    return render_template('index.html', username=username)


@app.route('/post/<int:post_id>')
def post(post_id: int):
    return f'{post_id=}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath: str):
    return f'{subpath=}'


@app.route('/redirect/')
def redirect_test():
    # /redirect -> /redirect/ にリダイレクトする
    return f'test'


@app.route('/unauthorized')
def show_401():
    abort(401)


@app.route('/notfound')
def show_404():
    abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
