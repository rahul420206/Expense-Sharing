from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


# In app.py or config.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/expense_tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, disables a warning

from flask_migrate import Migrate
from models import db
migrate = Migrate(app, db)


# Initialize database
db = SQLAlchemy(app)

# Initialize the database
db.init_app(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mobile = db.Column(db.String(15), unique=True, nullable=False)

# Expense model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    split_method = db.Column(db.String(50), nullable=False)
    details = db.Column(db.JSON, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('expenses', lazy=True))

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

# API to get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email, 'mobile': user.mobile} for user in users])

@app.route('/api/add_user', methods=['POST'])
def add_user():
    try:
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        new_user = User(name=name, email=email, mobile=mobile)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully!"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})

# API to delete a user
@app.route('/api/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully!"})
    return jsonify({"error": "User not found!"})

# API to get all expenses
@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([{
        'id': exp.id,
        'description': exp.description,
        'amount': exp.amount,
        'split_method': exp.split_method,
        'details': exp.details
    } for exp in expenses])

# API to add an expense
@app.route('/api/add_expense', methods=['POST'])
def add_expense():
    try:
        description = request.form['description']
        amount = float(request.form['amount'])
        split_method = request.form['split_method']
        details = request.form['details']
        user_id = 1  # Modify as needed

        new_expense = Expense(
            description=description,
            amount=amount,
            split_method=split_method,
            details=eval(details),
            user_id=user_id
        )
        db.session.add(new_expense)
        db.session.commit()
        return jsonify({"message": "Expense added successfully!"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})

# API to delete an expense
@app.route('/api/delete_expense/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    expense = Expense.query.get(expense_id)
    if expense:
        db.session.delete(expense)
        db.session.commit()
        return jsonify({"message": "Expense deleted successfully!"})
    return jsonify({"error": "Expense not found!"})

if __name__ == '__main__':
    app.run(debug=True)
