from markupsafe import escape
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/hello/<string:name>')
def home(name=None):
    return render_template('hello.html', name=name)


@app.route('/<name>')
def hello(name):
    return f"Hello, {escape(name).title()}!"


@app.route('/user/<username>')
def show_profile(username):
    return f"Your profile is {username}"


@app.route('/post/<int:id>')
def show_post(id):
    return f"Post {id}"


@app.route('/post/<string:id>')
def show_post_str(id):
    return f"Post String {id}"


@app.route('/path/<path:subpath>')
def show_path(subpath):
    return f"Your subpath is {subpath}"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_login()
    else:
        return show_login()


def do_login():
    return "Login"


def show_login():
    return "login form"


if __name__ == '__main__':  #digunakan apabila file py di run sebagai standalone "py app.py"
    app.run(debug=true)