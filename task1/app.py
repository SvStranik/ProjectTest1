from flask import Flask, render_template

from data import generate_users

users = generate_users(100)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN (write your solution here)
@app.route('/users')
def get_users():
    return render_template('users/index.html', users=users)


@app.route('/users/<int:id>')
def get_first_name(id):
    user = [user for user in users if user["id"] == id]
    if user == []:
        return ('Page not found', 404)
    return render_template('users/show.html', user=user[0])
# END
