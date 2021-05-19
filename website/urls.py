from django.shortcuts import render
from django.urls import path

from . import views

app_name = "website"


urlpatterns = [
    path('', views.home_page_view, name="home"),
    path('pagina1', views.pagina1_page_view, name="pagina1"),
    path('pagina2', views.pagina2_page_view, name="pagina2")
]