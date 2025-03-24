from django.urls import path, include
from board import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('workers/', views.workers, name='workers'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]
