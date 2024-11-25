from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import serializers
import json

# Globale Liste für Shopping-Items (Simulation einer Datenbank)
shopping_items = []

# Serializer für Shopping-Items zur Swagger-Dokumentation und Validierung
class ShoppingItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, help_text="Name of the shopping item")
    amount = serializers.IntegerField(help_text="Amount of the shopping item")

# Beispiel zum Testen - einfacher HTTP-Response
def hello_world(request):
    return HttpResponse("Hello, World!")

# GET: Alle Shopping-Items abrufen
@swagger_auto_schema(
    method='get',
    operation_summary="Retrieve all shopping items",
    operation_description="Returns a list of all shopping items.",
    responses={200: ShoppingItemSerializer(many=True)}
)
@api_view(['GET'])
def get_all_items(request):
    return Response(shopping_items, status=status.HTTP_200_OK)

# POST: Neues Shopping-Item hinzufügen
@swagger_auto_schema(
    method='post',
    operation_summary="Add a new shopping item",
    operation_description="Creates a new shopping item with the specified name and amount.",
    request_body=ShoppingItemSerializer,
    responses={
        201: openapi.Response("Item successfully created.", ShoppingItemSerializer),
        400: "Invalid input"
    }
)
@api_view(['POST'])
def add_item(request):
    serializer = ShoppingItemSerializer(data=request.data)
    if serializer.is_valid():
        shopping_items.append(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET: Ein Shopping-Item nach Name abrufen
@swagger_auto_schema(
    method='get',
    operation_summary="Retrieve a shopping item by name",
    operation_description="Fetches the shopping item with the specified name.",
    manual_parameters=[
        openapi.Parameter(
            'name', openapi.IN_PATH,
            description="Name of the shopping item",
            type=openapi.TYPE_STRING
        )
    ],
    responses={
        200: ShoppingItemSerializer,
        404: "Item not found"
    }
)
@api_view(['GET'])
def get_item_by_name(request, name):
    item = next((item for item in shopping_items if item['name'] == name), None)
    if item:
        return Response(item, status=status.HTTP_200_OK)
    return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

# PUT: Ein bestehendes Shopping-Item aktualisieren
@swagger_auto_schema(
    method='put',
    operation_summary="Update an existing shopping item",
    operation_description="Updates the amount of the shopping item with the specified name.",
    manual_parameters=[
        openapi.Parameter(
            'name', openapi.IN_PATH,
            description="Name of the shopping item to update",
            type=openapi.TYPE_STRING
        )
    ],
    request_body=ShoppingItemSerializer,
    responses={
        200: openapi.Response("Item updated successfully.", ShoppingItemSerializer),
        404: "Item not found",
        400: "Invalid input"
    }
)
@api_view(['PUT'])
def update_item(request, name):
    serializer = ShoppingItemSerializer(data=request.data)
    if serializer.is_valid():
        for item in shopping_items:
            if item['name'] == name:
                item['amount'] = serializer.validated_data['amount']
                return Response(item, status=status.HTTP_200_OK)
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE: Ein Shopping-Item löschen
@swagger_auto_schema(
    method='delete',
    operation_summary="Delete a shopping item by name",
    operation_description="Removes the shopping item with the specified name.",
    manual_parameters=[
        openapi.Parameter(
            'name', openapi.IN_PATH,
            description="Name of the shopping item to delete",
            type=openapi.TYPE_STRING
        )
    ],
    responses={
        204: "Item deleted successfully.",
        404: "Item not found"
    }
)
@api_view(['DELETE'])
def delete_item(request, name):
    global shopping_items
    initial_count = len(shopping_items)
    shopping_items = [item for item in shopping_items if item['name'] != name]
    if len(shopping_items) < initial_count:
        return Response({"message": "Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
