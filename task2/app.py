from flask import Flask, redirect, render_template, request

from user import generate_users

users = generate_users(5)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/users', methods=['GET'])
def get_users():
    return render_template('users/index.html', users=users)


# BEGIN (write your solution here)
@app.route('/users/create', methods=['GET'])
def get_create():
    return render_template('users/create.html')


@app.route('/users', methods=['POST', 'PUT'])
def post_create():
    username = request.form['first_name']
    surname = request.form['last_name']
    if username and surname:
        users.append({
                'first_name': username,
                'last_name': surname,
            })
        return redirect('/users')
    elif not username:
        return "First name can't be blank", 422
    else:
        return "Last name can't be blank", 422
# END
