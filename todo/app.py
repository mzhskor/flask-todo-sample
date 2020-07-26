from flask import Flask, url_for, render_template
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
