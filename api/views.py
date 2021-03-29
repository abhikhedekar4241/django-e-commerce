from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, JsonResponse
from .handler import Handler
from .models import Category
import json


@csrf_exempt
def categoryController(request: HttpRequest, id=False):
    handler = Handler[Category]()
    if request.method == 'GET':
        # if id is not false then return single document
        if id != False:
            document = Category.objects(id=id)
            jsonDocument = json.loads(document.to_json())
            return JsonResponse({'data': jsonDocument, 'id': id})

        documents = Category.objects
        jsonDocuments = json.loads(documents.to_json())
        return JsonResponse({'data': jsonDocuments, 'id': id})

    elif request.method == 'POST':
        decodedBody = json.loads(request.body)
        document = Category(name=decodedBody['name'])
        document.save()
        jsonDocument = json.loads(document.to_json())
        return JsonResponse({'data': jsonDocument, 'id': id})

    elif request.method == 'PUT':
        document = json.dumps(Category.objects(_id=id))
        document = request.body
        document.save()
        return JsonResponse({'data': document, 'id': id})

    elif request.method == 'DELETE':
        document = json.dumps(Category.objects(_id=id))
        document.delete()
        return JsonResponse({'message': 'deleted'})

    return HttpResponse('Somwthing went wrong.')


@csrf_exempt
def template(request: HttpRequest, id=False):
    if request.method == 'GET':
        # if id is not false.
        if id:
            return HttpResponse(id)
        return HttpResponse('Get done')

    elif request.method == 'POST':
        return HttpResponse('POST done')

    elif request.method == 'PUT':
        return HttpResponse('PUT done')

    elif request.method == 'DELETE':
        return HttpResponse('DELETE done')

    return HttpResponse('Somwthing went wrong.')
