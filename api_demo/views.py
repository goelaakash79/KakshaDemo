from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
# Create your views here.
def markAttendance(request):
    if request.method == 'GET':
        data = {"ji":5}
    return JsonResponse(data)

def getStudents(request):
    if request.method == 'GET':
        query_get_students =  Student.objects.values()
        data = list(query_get_students)
    return JsonResponse({"students":data}, safe=False)
