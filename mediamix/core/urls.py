from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

# Create your views here.
app_name = "core"
urlpatterns = [
    path("",views.index, name="index"),
    path("sobremi",views.sobremi, name="sobremi"),
    path('login', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('register', views.Register.as_view(template_name='core/register.html'), name='register'),
    path('profile', views.Profile.as_view(template_name='core/profile.html'), name='profile'),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)