from django.shortcuts import render
from json import JSONDecodeError
from django.http import JsonResponse, HttpResponse
from .serializers import ContactSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from .models import *
from django.views.generic import TemplateView

# Create your views here.

class ContactAPIView(views.APIView):
    def post(self, request):
        data = request.data
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)