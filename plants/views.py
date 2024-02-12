from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_plants(request):
    return render(request, 'plants/my_plants.html')  