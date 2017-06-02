from pymongo import TEXT
from pymodm import connect, fields, MongoModel

from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField

import mistune

connect('mongodb://localhost:27017/oktki')


class Page(MongoModel):
    title = fields.CharField()
    body = fields.CharField(blank=True)

    @staticmethod
    def get(title):
        return Page.objects.raw({'title': title}).first()

    @staticmethod
    def create(title):
        return Page(title=title, body='').save()

    def update(self, body):
        self.body = body
        self.save()

    @property
    def markdown(self):
        return mistune.markdown(self.body)


class CreatePageForm(FlaskForm):
    title = StringField('Title')
    submit = SubmitField()


class EditPageForm(FlaskForm):
    body = TextAreaField('Edit Content')
    submit = SubmitField()

