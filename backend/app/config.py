import os

class SystemConfig:
  DEBUG = True

MYSQL_PASS = os.environ['MYSQL_PASSWORD']

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}?charset=utf8'.format(**{
    'user': "flask",
    'password': MYSQL_PASS,
    'host': "db",
    'port': "3306",
    'db_name': "flask-app"
})

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.urandom(24)

Config = SystemConfig
