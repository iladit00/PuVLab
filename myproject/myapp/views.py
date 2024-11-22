from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import serializers
import json


# Beispiel zum Testen - einfacher HTTP-Response
def hello_world(request):
    return HttpResponse("Hello, World!")

def hello(request):
    return HttpResponse("Hello, Django!")

# Globale Liste für Shopping-Items (Simulation einer Datenbank)
shopping_items = []

# Serializer für Shopping-Items zur Swagger-Dokumentation und Validierung
class ShoppingItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    amount = serializers.IntegerField()

# GET: Alle Shopping-Items abrufen
@swagger_auto_schema(method='get', responses={200: ShoppingItemSerializer(many=True)})
@api_view(['GET'])
def get_all_items(request):
    return Response(shopping_items, status=status.HTTP_200_OK)

# POST: Neues Shopping-Item hinzufügen
@swagger_auto_schema(method='post', request_body=ShoppingItemSerializer, responses={201: 'Item successfully created', 400: 'Invalid input'})
@api_view(['POST'])
def add_item(request):
    try:
        serializer = ShoppingItemSerializer(data=request.data)
        if serializer.is_valid():
            shopping_items.append(serializer.data)
            return Response({"message": "Item successfully created."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except json.JSONDecodeError:
        return Response({"error": "Invalid JSON data"}, status=status.HTTP_400_BAD_REQUEST)

# GET: Ein Shopping-Item nach Name abrufen
@swagger_auto_schema(method='get', responses={200: ShoppingItemSerializer, 404: 'Item not found'})
@api_view(['GET'])
def get_item_by_name(request, name):
    item = next((item for item in shopping_items if item['name'] == name), None)
    if item:
        return Response(item, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

# PUT: Ein bestehendes Shopping-Item aktualisieren
@swagger_auto_schema(method='put', request_body=ShoppingItemSerializer, responses={200: 'Item updated successfully', 404: 'Item not found', 400: 'Invalid JSON'})
@api_view(['PUT'])
def update_item(request, name):
    try:
        serializer = ShoppingItemSerializer(data=request.data)
        if serializer.is_valid():
            for item in shopping_items:
                if item['name'] == name:
                    item["amount"] = serializer.validated_data["amount"]
                    return Response({"message": "Item updated successfully."}, status=status.HTTP_200_OK)
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)

# DELETE: Ein Shopping-Item löschen
@swagger_auto_schema(method='delete', responses={204: 'Item deleted successfully', 404: 'Item not found'})
@api_view(['DELETE'])
def delete_item(request, name):
    global shopping_items
    initial_count = len(shopping_items)
    shopping_items = [item for item in shopping_items if item['name'] != name]
    if len(shopping_items) < initial_count:
        return Response({"message": "Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
