from django.urls import include, path
from rango import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
