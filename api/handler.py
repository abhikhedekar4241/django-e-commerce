from django.http import JsonResponse, HttpRequest, QueryDict
from mongoengine import Document
import json


def getOne(Model,  id):
    document = Model.objects.with_id(id)
    converted = document.getDict()
    return send_response(converted, 'Document fetched successfully.')


def getMultiple(Model, request: HttpRequest):
    converted = []
    searchFilter = {}
    s_id = request.GET.get('subCategoryId')
    if s_id != None:
        searchFilter['subCategoryId'] = s_id

    c_id = request.GET.get('categoryId')
    if c_id != None:
        searchFilter['categoryId'] = c_id

    all_objects = Model.objects(__raw__=searchFilter)
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
