from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "peliculas"


urlpatterns = [
    path("", views.index, name="index"),
    path("peliculas/list", views.PeliculaList.as_view(), name="peliculas_list"),
    path("peliculas/create", views.PeliculaCreate.as_view(), name="peliculas_create"),
    path("director/list", views.DirectorList.as_view(), name="director_list"),
    path("peliculas/detail/<int:pk>", views.PeliculaDetail.as_view(), name="peliculas_detail"),
    path("director/detail/<int:pk>", views.DirectorDetail.as_view(), name="director_detail"),
    path("peliculas/update/<int:pk>", views.PeliculaUpdate.as_view(), name="peliculas_update"),
    path("peliculas/delete/<int:pk>", views.PeliculaDelete.as_view(), name="peliculas_delete"),

    ]