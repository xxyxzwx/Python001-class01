from django.urls import path
from . import views

urlpatterns = [
    path('index', views.test),
    path('result', views.result),
    path('test', views.searchtest),
]
