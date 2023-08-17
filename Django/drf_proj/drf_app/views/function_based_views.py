from django.shortcuts import render, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ..serializer import *
from ..models import *
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        stu_objs = Student.objects.all()
        stu_serl = StudentSerializer(stu_objs, many = True)
        json_byte_data = JSONRenderer().render(stu_serl.data)
        
        return HttpResponse(json_byte_data, content_type='application/json')
    
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            json_data= JSONRenderer().render(serializer.data)
        else:
            json_data = JSONRenderer().render(serializer.errors)
            
        return HttpResponse(json_data ,content_type="application/json")

@csrf_exempt
def student_detail_api(request,pk):
    if request.method == 'GET':
        stu_objs = Student.objects.get(id=pk)
        stu_serl = StudentSerializer(stu_objs)
        json_byte_data = JSONRenderer().render(stu_serl.data)
        
        return HttpResponse(json_byte_data, content_type='application/json')
        
    if request.method =="PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        stud_obj = Student.objects.get(id=pk)
        serializer = StudentSerializer(stud_obj, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            json_data= JSONRenderer().render(serializer.data)
        else:
            json_data = JSONRenderer().render(serializer.errors)
            
        return HttpResponse(json_data ,content_type="application/json")
    if request.method == 'DELETE':
        stud_obj = Student.objects.get(id=pk)
        serializer = StudentSerializer(stud_obj)
        res = {
            'msg': "Data was deleted."
        }
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type="application/json")