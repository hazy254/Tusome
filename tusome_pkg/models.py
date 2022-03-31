#TODO: User, Book, Review, Preferences
from encodings import utf_8
from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin

bcrypt = Bcrypt()
db = SQLAlchemy()



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable= False)
    password_hash = db.Column(db.String(60), nullable=False)
    #books = db.relationship('Book', backref='owner', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf_8')

    def check_password_correction(self, password_attempt):
        return bcrypt.check_password_hash(self.password_hash, password_attempt)
            
    
    def __repr__(self) -> str:
        return f'User: {self.username}'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(400), nullable=False)
    author = db.Column(db.String(120),nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    #TODO: COVER
    #reviews = db.relationship('Review', backref='reviewer', lazy=True)

#TODO: OWNERS

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    book_review = db.Column(db.String(2028))
    #TODO: Foreign_key for reviewer, book

