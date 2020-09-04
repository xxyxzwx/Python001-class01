from django.urls import path
from . import views

urlpatterns = [
    path('', views.result),
    path('result', views.result),
    path('search', views.searchtest),
    path('allcomment', views.allcomment),
]
