from django.urls import path

from . import views

app_name = 'app_games'

urlpatterns = [
 path('principal', views.principal, name='principal'),	

]