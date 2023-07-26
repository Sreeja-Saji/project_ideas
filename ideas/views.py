from django.shortcuts import render
# from django.http import HttpResponse
# from.models import Course
# from.models import Project_Ideas
# from.models import Technology

# Create your views here.
def new(request):
    return render(request,'form.html')
