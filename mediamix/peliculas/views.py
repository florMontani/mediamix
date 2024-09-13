from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Peliculas, Director
from .forms import PeliculasForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def index(request):
    return render(request,'peliculas/index.html')



#PELICULAS

#List
class PeliculaList(LoginRequiredMixin,ListView):
    model = Peliculas
    context_object_name = 'peliculas'
    def get_queryset(self):
        queryset =  super().get_queryset() #Peliculas.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset = Peliculas.objects.filter(nombre__icontains=query)
        return queryset  
      
#Create
class PeliculaCreate(LoginRequiredMixin,CreateView):
    model = Peliculas
    form_class = PeliculasForm
    template_name = 'peliculas/peliculas_create.html'
    success_url = reverse_lazy('peliculas:peliculas_list')


#Detail
class PeliculaDetail(LoginRequiredMixin,DetailView):
    model = Peliculas


#Update
class PeliculaUpdate(LoginRequiredMixin,UpdateView):
    model = Peliculas
    form_class = PeliculasForm
    template_name = 'peliculas/peliculas_create.html'
    success_url = reverse_lazy('peliculas:peliculas_list')
  

#Delete    
class PeliculaDelete(LoginRequiredMixin,DeleteView):
    model = Peliculas
    success_url = reverse_lazy('peliculas:peliculas_list')


# DIRECTOR

# create "create","update", delete.
#List
class DirectorList(LoginRequiredMixin,ListView):
    model = Director
    context_object_name = 'director'
 
    def get_queryset(self):
        queryset =  super().get_queryset() #Director.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset = Director.objects.filter(nombre__icontains=query)
        return queryset  
    
#Details
class DirectorDetail(LoginRequiredMixin,DetailView):
    model = Director
