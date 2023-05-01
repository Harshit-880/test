from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.

class ListToDo(generics.ListAPIView):                  #read
    queryset = ToDo.objects.all()
    serializer_class = ToDOSerializer
    

class DetailToDo(generics.RetrieveUpdateAPIView):         #Update
    queryset = ToDo.objects.all()
    serializer_class = ToDOSerializer


class CreateToDo(generics.CreateAPIView):                #create
    queryset = ToDo.objects.all()
    serializer_class = ToDOSerializer


class DeleteToDo(generics.DestroyAPIView):                #delete
    queryset = ToDo.objects.all()
    serializer_class = ToDOSerializer