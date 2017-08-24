from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import LONGTEXT
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:letsplay@localhost:3306/trialdata'
app.config['SECRET_KEY'] = 'po_dummy_secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Questions(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(LONGTEXT)
    added = db.Column(db.DateTime)
    option = db.relationship('Options', back_populates='question')

    def __init__(self, body):
        self.body = body
        self.added = datetime.now()


class Options(db.Model):
    __tablename__ = 'option'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    body = db.Column(LONGTEXT)
    question = db.relationship('Questions', back_populates='option')

    def __init__(self, body, question_id):
        self.body = body
        self.question_id = question_id
