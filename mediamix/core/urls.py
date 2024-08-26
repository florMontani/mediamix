from django.urls import path
from . import views
# Create your views here.
app_name = "core"
urlpatterns = [
    path("",views.index, name="index"),
]
