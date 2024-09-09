from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Peliculas, Director
from .forms import PeliculasForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request,'peliculas/index.html')



#PELICULAS

#List
class PeliculaList(ListView):
    model = Peliculas
    context_object_name = 'peliculas'
    def get_queryset(self):
        queryset =  super().get_queryset() #Peliculas.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset = Peliculas.objects.filter(nombre__icontains=query)
        return queryset  
      
#Create
class PeliculaCreate(CreateView):
    model = Peliculas
    form_class = PeliculasForm
    template_name = 'peliculas/peliculas_create.html'
    success_url = reverse_lazy('peliculas:peliculas_list')

#Detail
class PeliculaDetail(DetailView):
    model = Peliculas 

#Update
class PeliculaUpdate(UpdateView):
    model = Peliculas
    form_class = PeliculasForm
    template_name = 'peliculas/peliculas_create.html'
    success_url = reverse_lazy('peliculas:peliculas_list')

#Delete    
# def peliculas_delete(request,pk:int):
#     query = Peliculas.objects.get(id=pk)
#     if request.method == 'POST':
#        query.delete()
#        return redirect('peliculas:peliculas_list')
#     return render(request,'peliculas/peliculas_confirm_delete.html',{'object':query})
class PeliculaDelete(DeleteView):
    model = Peliculas
    success_url = reverse_lazy('peliculas:peliculas_list')


    


# DIRECTOR

#List
class DirectorList(ListView):
    model = Director
    context_object_name = 'director'
    def get_queryset(self):
        queryset =  super().get_queryset() #Director.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset = Director.objects.filter(nombre__icontains=query)
        return queryset  

def director_detail(request, pk:int):
    query = Director.objects.get(id=pk)
    return render(request,'peliculas/director_detail.html',{'object':query}) 