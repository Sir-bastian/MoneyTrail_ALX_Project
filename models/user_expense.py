#!/usr/bin/python3
'''A script that handles the users and expenses tables in the
database. The relationships between the tables are established
using foreign keys and relationship attributes.
'''

from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    '''Represents a user in the application'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    expenses = db.relationship('Expense', backref='user', lazy=True)

    def set_password(self, password):
        '''
        method that takes a plain text password as input
        and generates its hash using the hash function. The resulting
        hash is then stored in the password_hash attribute of the User
        instance
        '''
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        '''
        Method to check if given password matches the hashed password stored
        in the password_hash attribute. The method returns True if passwords
        match, indictaing that the provided password is correct.
        '''
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        '''String representation of a user object. It returns
        a formated string with the name of the user'''
        return f'<User {self.username}>'

class Expense(db.Model):
    '''
    Represents an expense entry in the application.
    '''
    id = db.Column(db.Integer, primary_key=true)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float(precision=2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        '''
        String representation of expense object. return a string with
        category and amount of expense.
        '''
        return f'<Expense {self.category}: {Self.amount}>'
