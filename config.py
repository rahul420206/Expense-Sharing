import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_URI')  # e.g., 'mysql+pymysql://user:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True

SECRET_KEY = 'e4f8d8cd432b469abc9d2c4ffdb1f322'
