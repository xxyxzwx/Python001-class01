from django.urls import path
from . import views

urlpatterns = [
    path('', views.result),
    path('result', views.result),
    path('test', views.searchtest),
]
