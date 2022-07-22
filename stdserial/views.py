from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
from serializers import Studentserializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

#Model Instance
def student_details(request,pk):
    std=Student.objects.get(id=pk)
    stdserializer=Studentserializer(std)
    json_data=JSONRenderer().render(stdserializer.data)
    return HttpResponse(json_data,content_type='application/json')

#Query Set
def student_list(request):
    std=Student.objects.all()
    stdserializer=Studentserializer(std, many=True)
    json_data=JSONRenderer().render(stdserializer.data)
    return HttpResponse(json_data,content_type='application/json')

