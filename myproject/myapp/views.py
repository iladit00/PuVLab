from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def hello_world(request):
    return HttpResponse("Hello, World!")
def hello(request):
    return HttpResponse("Hello, Django!")

shopping_items = []

@csrf_exempt
def get_item_by_name(request, name):
    if request.method == 'GET':
        item = next((item for item in shopping_items if item['name'] == name), None)
        if item:
            return JsonResponse(item)
        else:
            return JsonResponse({'error': 'Item not found'}, status=404)
        
@csrf_exempt
def update_item(request, name):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            for item in shopping_items:
                if item['name'] == name:
                    item["amount"] = data["amount"]
                    return JsonResponse({"message": "Item updated successfully."})
        except json.JSONDecodeError:
           return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
@csrf_exempt
def delete_item(request, name):
    if request.method == 'DELETE':
        global shopping_items
        shopping_items = [item for item in shopping_items if item['name'] != name]
        return JsonResponse({"message": "Item deleted successfully."}, status=204)

@csrf_exempt
def get_all_items(request):
    if request.method == 'GET':
        return JsonResponse(shopping_items, safe=False)

@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            shopping_items.append(data)
            return JsonResponse({"message": "Item successfully created."}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)