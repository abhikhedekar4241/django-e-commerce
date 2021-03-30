from mongoengine import fields, Document, EmbeddedDocumentField, EmbeddedDocument
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
    active = fields.BooleanField(default=True)
    description = fields.StringField(max_length=100)

    def create(self, params):
        super(SubCategory, self).__init__()
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


class ItemOption(EmbeddedDocument):
    name = fields.StringField(max_length=50)
    quality = fields.IntField()
    unit = fields.StringField(max_length=50)
    group = fields.StringField(max_length=50)
    price = fields.IntField()
    stock = fields.IntField()
    discount = fields.IntField()
    discountUnit = fields.StringField(max_length=50)

    def create(self, params):
        super(ItemOption, self).__init__()
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


class Item(Document):
    name = fields.StringField()
    image = fields.StringField(default='https://picsum.photos/200',)
    active = fields.BooleanField(default=True)
    featured = fields.BooleanField(default=True)
    # options = fields.ListField(EmbeddedDocumentField(ItemOption))
    description = fields.StringField(max_length=100)
    categoryId = fields.ObjectId()
    subCategoryId = fields.ObjectId()

    def create(self, params):
        super(Item, self).__init__()
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
