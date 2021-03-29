from mongoengine import fields, Document
import datetime


class Category(Document):
    name = fields.StringField()
