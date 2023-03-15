from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
import os
import openai
from django.http import JsonResponse
import json

def create_jsonl():
    dic_exm ={
       'prompt': 'data', 'completion': 'completion'
    }
    json_obj = json.dumps(dic_exm)
    with open("example.jsonl", "w") as outfile:
        outfile.write(json_obj)


class FineTunningViewSet(viewsets.ModelViewSet):
    
    @action(methods=['POST'], detail=False, url_path='create-bucket', url_name='create_bucket')
    def post(self, request, pk=None):
        create_jsonl()
        openai.api_key = "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"
        
        response = openai.File.create(
            file=open("example.jsonl", "rb"),
            purpose='fine-tune'
        )
        
        print("******************* response ")
        print(response)
        return JsonResponse({"engines": "engines"})
    
    @action(methods=['DELETE'], detail=False, url_path='create-bucket', url_name='create_bucket')
    def delete(self, request, pk=None):
        openai.api_key = "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"
        response = openai.File.delete("file-F9UerO2SXt0EEscUsqFIZZoV")
        print("******************* response ")
        print(response)
        return JsonResponse({"engines": "engines"})
    
    @action(methods=['GET'], detail=False, url_path='create-training', url_name='create_training')
    def training(self, request, pk=None):
        openai.api_key = "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"
        response = openai.FineTune.create(training_file="file-VOINFf87UIBHqmbmecz2ZCmc")
        print("******************* response ")
        print(response)
        return JsonResponse({"engines": "engines"})
    
    @action(methods=['POST'], detail=False, url_path='create-training', url_name='create_training')
    def engine(self, request, pk=None):
        openai.api_key = "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"
        response = openai.Completion.create(
                model='ft-KoXC0DWKgdCYadMGoJ0oQ3gO',
                prompt="how are you?")
        print("******************* response ")
        print(response)
        return JsonResponse({"engines": "engines"})
    

    @action(methods=['GET'], detail=False, url_path='create-training-list', url_name='create_training')
    def fine_tunning(self, request, pk=None):
        openai.api_key = "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"
        response = openai.FineTune.list_events(id="ft-KoXC0DWKgdCYadMGoJ0oQ3gO")
        print("******************* response ")
        print(response)
        return JsonResponse({"engines": "engines"})
    
    @action(methods=['GET'], detail=False, url_path='create-ai', url_name='create_training')
    def fine_tunning(self, request, pk=None):
        openai.api_key = "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"
        response = openai.Completion.create(
            model="curie",
            prompt="como estas?")
        print("******************* response ")
        print(response)
        return JsonResponse({"engines": "engines"})