from django.urls import path
from . import views

app_name = "peliculas"


urlpatterns = [
    path("", views.index, name="index"),
    path("peliculas/list", views.peliculas_list, name="peliculas_list"),
    path("peliculas/create", views.peliculas_create, name="peliculas_create"),
    path("director/list", views.director_list, name="director_list"),
    ]