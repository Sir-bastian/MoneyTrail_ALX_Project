from flask import Flask, request, jsonify
import mysql.connector
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()
# Establish MySQL database connection
db = mysql.connector.connect(
    host='localhost',
    user='moneytrail',
    password='branham@27',
    database='moneytrail_db'
)
cursor = db.cursor()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401

    session['user_id'] = user.id
    return jsonify({'message': 'Login successful'}), 200

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'}), 200

@app.route('/expenses', methods=['POST'])
def add_expense():
    if 'user_id' not in session:
        return jsonify({'message': 'User not logged in'}), 401

    data = request.get_json()
    description = data.get('description')
    amount = data.get('amount')

    if not description or not amount:
        return jsonify({'message': 'Description and amount are required'}), 400

    user_id = session['user_id']
    expense = Expense(description=description, amount=amount, user_id=user_id)
    db.session.add(expense)
    db.session.commit()

    return jsonify({'message': 'Expense added successfully'}), 201

@app.route('/expenses', methods=['GET'])
def get_all_expenses():
    if 'user_id' not in session:
        return jsonify({'message': 'User not logged in'}), 401

    user_id = session['user_id']
    expenses = Expense.query.filter_by(user_id=user_id).all()

    return jsonify([expense.serialize() for expense in expenses]), 200

@app.route('/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    if 'user_id' not in session:
        return jsonify({'message': 'User not logged in'}), 401

    expense = Expense.query.get(expense_id)
    if not expense:
        return jsonify({'message': 'Expense not found'}), 404

    if expense.user_id != session['user_id']:
        return jsonify({'message': 'Unauthorized to update this expense'}), 403

    data = request.get_json()
    description = data.get('description')
    amount = data.get('amount')

    if description:
        expense.description = description
    if amount:
        expense.amount = amount

    db.session.commit()

    return jsonify({'message': 'Expense updated successfully'}), 200

@app.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    if 'user_id' not in session:
        return jsonify({'message': 'User not logged in'}), 401

    expense = Expense.query.get(expense_id)
    if not expense:
        return jsonify({'message': 'Expense not found'}), 404

    if expense.user_id != session['user_id']:
        return jsonify({'message': 'Unauthorized to delete this expense'}), 403

    db.session.delete(expense)
    db.session.commit()

    return jsonify({'message': 'Expense deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
