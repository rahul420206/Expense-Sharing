# Expense Sharing app

This project is an Expense Tracker web application built with Flask. It allows users to manage their expenses by adding, deleting, and viewing their data.

## Features

- User management (add and delete users)
- Expense tracking (add and delete expenses)
- API endpoints for user and expense data

## Requirements

- Python 3.x
- MySQL server

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

Edit the config.py file to set up your MySQL database URI and secret key.
You can also use environment variables by creating a .env file:
MYSQL_URI=mysql://root:@localhost/expense_tracker
SECRET_KEY=your_secret_key

initialize your db:
flask db init
flask db migrate
flask db upgrade

run the app:
python app.py
