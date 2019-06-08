import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'temp'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://qspvembvslzvmq:757dde21def9903c1b378d310c6297f6679a3e9998ced0b11ce124a06512f445@ec2-54-83-205-27.compute-1.amazonaws.com:5432/dbg8ue19v7u6jf'
