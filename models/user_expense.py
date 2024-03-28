#!/usr/bin/python3
'''A script that handles the users and expenses tables in the
database. The relationships between the tables are established
using foreign keys and relationship attributes.
'''

from app import db


class User(UserMixin, db.Model):
    '''Represents a user in the application'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    expenses = db.relationship('Expense', backref='user', lazy=True)

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
