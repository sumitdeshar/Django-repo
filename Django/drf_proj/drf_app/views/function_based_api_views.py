from django.shortcuts import render, HttpResponse
<<<<<<< HEAD
from rest_framework.renderers import JSONRenderer,status
=======
from rest_framework.renderers import JSONRenderer
>>>>>>> c2ad93beaa4d06ddc8d85e16a42d16298a40afc7
from rest_framework.parsers import JSONParser
from ..serializer import *
from ..models import *
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

<<<<<<< HEAD

=======
>>>>>>> c2ad93beaa4d06ddc8d85e16a42d16298a40afc7
# Create your views here.

@api_view(["GET", "POST", "PUT", "DELETE"])
def StudentAPI(request):
    
    if request.method == "GET":
        pythondata = request.data
        id = pythondata.get("id", None)

        if id is not None:
            stu_obj = Student.objects.get(id = id)
            stu_seri = StudentSerializer(stu_obj)
            return Response(stu_seri.data)

        stu_obj = Student.objects.all()
        stu_seri = StudentSerializer(stu_obj, many=True)
        return Response(stu_seri.data)

    elif request.method == "POST":
        pythondata = request.data
        stu_seri = StudentSerializer(stu_obj)
        if stu_seri.is_valid():
            stu_seri.save()
            return Response(stu_seri.data)
        else:
<<<<<<< HEAD
            return Response(stu_seri.errors,status=status.HTTP_404_NOT_FOUND)
=======
            return Response(stu_seri.errors)
>>>>>>> c2ad93beaa4d06ddc8d85e16a42d16298a40afc7
        
    elif request.method == "PUT":
        pythondata = request.data
        id = pythondata.get("id", None)
        stu_obj = Student.objects.get(id = id)
        stu_seri = StudentSerializer(stu_obj, data=pythondata)
        if stu_seri.is_valid():
            stu_seri.save()
            return Response(stu_seri.data)
        else:
            return Response(stu_seri.errors)
        
    elif request.method == 'DELETE':
        pythondata = request.data
        id = pythondata.get("id", None)
        stu_obj = Student.objects.get(id = id)
        stu_obj.delete()
        response = {
            "msg": "your data has beeen deletedddddd...."
        }
        return Response(response)

