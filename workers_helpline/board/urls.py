from django.urls import path, include
from board import views
urlpatterns = [
    path('', views.index, name='index'),
    path('workers', views.workers, name='workers'),
    path('workers/unskilled', views.unskilled, name='unskilled'),
    path('workers/skilled', views.skilled, name='skilled'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]
