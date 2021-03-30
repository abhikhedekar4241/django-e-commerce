from django.http import JsonResponse
from mongoengine import Document
import json


def getOne(Model,  id):
    document = Model.objects.with_id(id)
    converted = document.getDict()
    return send_response(converted, 'Document fetched successfully.')


def getMultiple(Model):
    converted = []
    all_objects = Model.objects
    for document in all_objects:
        converted.append(document.getDict())

    return JsonResponse({'total': len(all_objects),
                         'message': 'Documents fetched successfully.', 'data': converted})


def createOne(Model, body):
    decodedBody = json.loads(body)
    document = Model().create(decodedBody)
    converted = document.getDict()
    return send_response(converted, 'Document created successfully.')


def updateOne(Model,  id, body):
    decodedBody = json.loads(body)
    document = Model.objects.with_id(id).update(decodedBody)
    converted = document.getDict()
    return send_response(converted, 'Document updated successfully.')


def deleteOne(Model,  id):
    document = Model.objects.with_id(id)
    document.delete()
    converted = document.getDict()
    return send_response(converted, 'Document deleted successfully.')


def send_response(data, message):
    return JsonResponse({'message': message, 'data': data})
