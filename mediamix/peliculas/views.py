from django.shortcuts import render, redirect
from .models import Peliculas, Director
from .forms import PeliculasForm

# Create your views here.
def index(request):
    return render(request,'peliculas/index.html')

def peliculas_list(request):
    query = request.GET.get("q")
    if query:
        peliculas = Peliculas.objects.filter(nombre__icontains=query)
    else:    
        peliculas = Peliculas.objects.all()
    return render(request,'peliculas/peliculas_list.html',{'peliculas': peliculas})

def peliculas_create(request):
    if request.method == 'GET':
        form = PeliculasForm()
    if request.method == 'POST':
        form = PeliculasForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("peliculas:peliculas_list")
            
    return render(request,'peliculas/peliculas_create.html',{'form':form})

def director_list(request):
    director = Director.objects.all()
    return render(request,'peliculas/director_list.html',{'director':director})