#!/usr/bin/python3
"""A script that initializes a flask application"""
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import mysql.connector
from flask_login import loginManager, UserMixin, login_user
from flask_login import login_required, lo_out_user, current_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key' #Need a secret key for secure sessions
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector:
           //username:password@localhost/moneytrail.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
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

@app.route('/home', methods=['GET'])
def home():
    ''' Returns user to home page '''
    pass

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    ''' Handle Sign in logic '''
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' handle login logic '''
    pass

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    ''' Handle logout requests '''
    pass
