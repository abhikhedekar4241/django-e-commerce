from mongoengine import fields, Document
import datetime
import json


class Category(Document):
    name = fields.StringField()
    image = fields.StringField()
    active = fields.BooleanField(default=True)
    description = fields.StringField()

    def create(self, params):
        super(Category, self).__init__()
        return self.update(params)

    def update(self, params):
        for key in params:
            super().__setattr__(key, params[key])
        super().save()
        return self

    def getDict(self):
        converted = json.loads(self.to_json())
        converted['_id'] = f'{self.pk}'
        return converted


class SubCategory(Document):
    name = fields.StringField(max_length=100)
    image = fields.StringField(max_length=100)
    category = fields.ObjectId()
    active = fields.BooleanField(required=True)
    description = fields.StringField(max_length=100)


class Item(Document):
    name = fields.StringField(max_length=100)
    image = fields.StringField(max_length=100)
    category = fields.ObjectId()
    active = fields.BooleanField(required=True)
    description = fields.StringField(max_length=100)
