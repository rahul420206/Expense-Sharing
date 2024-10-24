# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'  # Ensure it matches your MySQL table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))  # Adjust the length as per your requirement
    email = db.Column(db.String(100), unique=True)
    mobile = db.Column(db.String(15))  # Adjust the length as per your requirement

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    split_method = db.Column(db.String(50), nullable=False)
    details = db.Column(db.JSON, nullable=False)  # JSON field to store split details
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('expenses', lazy=True))
