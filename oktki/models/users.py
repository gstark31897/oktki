from pymongo import TEXT
from pymodm import connect, fields, MongoModel

from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField

from . import crypto

import mistune

connect('mongodb://localhost:27017/oktki')


class User(MongoModel):
    name = fields.CharField()
    hash = fields.CharField()
    salt = fields.CharField()
    hash_version = fields.IntField()
    logged_in = fields.BoolField()

    @staticmethod
    def get(name):
        return User.objects.raw({'name': name}).first()

    @staticmethod
    def create(name, password):
        salt = crypto.create_salt()
        hash = crypto.hash_password(password, salt)
        return User(name=name, hash=hash, salt=salt, hash_version=1, logged_in=False).save()

    def authenticate(self, password):
        hash = crypto.has_password(password, self.salt)
        return hash = self.hash

