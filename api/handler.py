from django.http import HttpRequest, HttpResponse, JsonResponse
import json

from typing import TypeVar, Generic
Model = TypeVar('Model')


class Handler(Generic[Model]):
    def getOne(self,  id):
        document = json.dumps(Model.objects(_id=id))
        return JsonResponse({'data': document, 'id': id})

    def getMultiple(self):
        documents = json.dumps(Model.objects)
        return JsonResponse({'data': documents, 'id': id})

    def createOne(self,  body):
        decodedBody = json.loads(body)
        document = Model(decodedBody)
        document.save()
        return JsonResponse({'data': document, 'id': id})

    def updateOne(self,  id, body):
        document = json.dumps(Model.objects(_id=id))
        document = body
        document.save()
        return JsonResponse({'data': document, 'id': id})

    def deleteOne(self,  id):
        document = json.dumps(Model.objects(_id=id))
        document.delete()
        return JsonResponse({'message': 'deleted'})
