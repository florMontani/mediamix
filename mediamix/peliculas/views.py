from django.shortcuts import render
from .models import Peliculas, Director

# Create your views here.
def index(request):
    return render(request,'peliculas/index.html')

def peliculas_list(request):
    peliculas = Peliculas.objects.all()
    return render(request,'peliculas/peliculas_list.html',{'peliculas': peliculas})

def director_list(request):
    director = Director.objects.all()
    return render(request,'peliculas/director_list.html',{'director':director})
