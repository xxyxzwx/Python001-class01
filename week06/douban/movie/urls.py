from django.urls import path
from . import views


urlpatterns = [
    path('index', views.pinglun),
    path('search', views.search, name='search'),
]
