from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse

def home(request):
    return render(request, 'home/index.html')

