from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student 
from .serializers import StudentSerializers
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    # if request.method == 'GET':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = Parser().paJSONrse(stream)
    #     id = pythondata.get('id',None)
    #     if id is not None:
    #         stu = Student.objects.get(id=id)
    #         serializers = StudentSerializers(stu)
    #         json_data = JSONRenderer().render(serializers.data)
    #         return HttpResponse(json_data, content_type= 'application/json')
    # stu = Student.objects.all()
    # serializers = StudentSerializers(stu,many=True)
    # json_data = JSONRenderer().render(serializers.data)
    # return HttpResponse(json_data,content_type='application/json')

    # if  request.method == 'POST':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     serializers = StudentSerializers(data = pythondata)
    #     if serializers.is_valid():
    #         serializers.save()
    #         res ={'msg':'Data created'}
    #         json_data = JSONRenderer().render(res)
    #         return HttpResponse(json_data, content_type='application/json')
    #     json_data = JSONRenderer.render(serializers.errors)
    #     return HttpResponse(json_data,content_type='application/json')
        
    if  request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializers(stu,data= pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Update !!'}
            json_data = JSONRenderer().render(res)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')   
        

    if  request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res={'msg':'data deleated'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')