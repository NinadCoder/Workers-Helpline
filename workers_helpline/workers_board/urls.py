from django.urls import path, include
from workers_board import views
urlpatterns = [
    path('', views.workers, name='workers'),
    path('unskilled', views.unskilled, name='unskilled'),
    path('skilled', views.skilled, name='skilled'),
    path('hire', views.hire, name='hire')
]
