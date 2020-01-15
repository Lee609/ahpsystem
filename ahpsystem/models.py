# -*- coding: utf-8 -*-
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ahpsystem import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(40))
    plan_name = db.Column(db.String(40))


class Standard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(40))
    standard_name = db.Column(db.String(40))