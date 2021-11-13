from app import db, login_manager
import os
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(256), nullable=False)
   
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)






class Phonebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name =  db.Column(db.String(150))
    phone = db.Column(db.String(150))
    email = db.Column(db.String(150))
    occupation = db.Column(db.String(150))
    address = db.Column(db.String(255))
   

    def __init__(self, first_name, last_name, phone, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone
        self.email = email
        self.address = address