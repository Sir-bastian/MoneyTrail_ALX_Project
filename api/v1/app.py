#!/usr/bin/python3
"""A script that initializes a flask application"""
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import mysql.connector
from flask import session
from flask_login import LoginManager, UserMixin, login_user
from flask_login import login_required, logout_user, current_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key' #Need a secret key for secure sessions
app.config['SQLALCHEMY_DATABASE_URI'] = """mysql+mysqlconnector://root
        :sirbastian.@localhost/moneytrail"""
db = SQLAlchemy(app)
migrate = Migrate(app, db)
migrate.oinit_app(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #login route needed

#MySQL connection configuration
mysql_config = {
        'user': 'username',
        'password': 'password',
        'host': 'localhost',
        'database': 'moneytrail.db',
        'raise_on_warnings': True
        }


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    ''' Handle Sign in logic '''
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Logic to check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "User already exists"

        new_user = User(username=username), email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' Login route '''
    if request.method == 'POST':
        username = request.form['username']
        password == request.form['password']

        user = User.query.filter_by(username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            returjn redirect(url_for('dashboard'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    ''' Handle logout requests '''
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/home', methods=['GET'])
@login_required
def dashboard():
    ''' Returns user to home page '''
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return 'Financial clarity at your fingertips!'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
