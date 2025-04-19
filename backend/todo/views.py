from django.shortcuts import render

from rest_framework import viewsets

from.serializers import TodoSerializer

from .models import Todo

class TodoView(viewsets.ModelViewSet):

    # Create a serializer class and
    # assign it to the TodoSerializer class
    serializer_class = TodoSerializer

    # Define a variable and populate it
    # with the TodoObject list objects
    queryset = Todo.objects.all()
