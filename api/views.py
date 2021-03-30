from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Category, SubCategory, Item
import json
from .handler import getOne, getMultiple, createOne, updateOne, deleteOne


@csrf_exempt
def categoryController(request: HttpRequest, id=False):
    if request.method == 'GET':
        # if id is not false then return single document
        if id != False:
            return getOne(Category, id)
        else:
            return getMultiple(Category)

    elif request.method == 'POST':
        return createOne(Category, request.body)

    elif request.method == 'PUT':
        return updateOne(Category, id, request.body)

    elif request.method == 'DELETE':
        return deleteOne(Category, id)

    return HttpResponse('Request not supported.')


@csrf_exempt
def subCategoryController(request: HttpRequest, id=False):
    if request.method == 'GET':
        # if id is not false then return single document
        if id != False:
            return getOne(SubCategory, id)
        else:
            return getMultiple(SubCategory)

    elif request.method == 'POST':
        return createOne(SubCategory, request.body)

    elif request.method == 'PUT':
        return updateOne(SubCategory, id, request.body)

    elif request.method == 'DELETE':
        return deleteOne(SubCategory, id)

    return HttpResponse('Request not supported.')


@csrf_exempt
def itemController(request: HttpRequest, id=False):
    if request.method == 'GET':
        # if id is not false then return single document
        if id != False:
            return getOne(Item, id)
        else:
            return getMultiple(Item)

    elif request.method == 'POST':
        return createOne(Item, request.body)

    elif request.method == 'PUT':
        return updateOne(Item, id, request.body)

    elif request.method == 'DELETE':
        return deleteOne(Item, id)

    return HttpResponse('Request not supported.')


def send_response(data, message):
    return JsonResponse({'message': message, 'data': data})
