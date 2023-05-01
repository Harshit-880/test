from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def home(request):
    student_object = Student.objects.all()
    serializer = StudentSerializer(student_object,many = True)

    return Response({'status': 200 , 'payload': serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data = request.data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':403, 'error': 'serializer.errors','message':'something went wrong'})
    serializer.save()

    return Response({'status': 200 , 'payload': serializer.data ,'message': 'you send'})


@api_view(['PUT'])
def update_student(request,id):
    try:
        student_obj = Student.objects.get(id = id)


        serializer = StudentSerializer(student_obj,data = request.data, partial = True)
 
        if not serializer.is_valid():
         print(serializer.errors)
         return Response({'status':403, 'error': 'serializer.errors','message':'something went wrong'})
        serializer.save()

        return Response({'status': 200 , 'payload': serializer.data ,'message': 'you send'})
    except Exception as e:
        print(e)
        return Response({'status':403, 'message':'invalid id'})