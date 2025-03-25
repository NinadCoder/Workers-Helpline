from django.urls import path, include
from workers_board import views
from .views import worker_profile
urlpatterns = [
    path('', views.workers, name='workers'),
    path('unskilled', views.unskilled, name='unskilled'),
    path('skilled', views.skilled, name='skilled'),
    path('hire', views.hire, name='hire'),
    path('worker/profile/', worker_profile, name='worker_profile')
]
