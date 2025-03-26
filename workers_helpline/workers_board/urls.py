from django.urls import path
from .views import workers, unskilled, skilled, hire

urlpatterns = [
    path('', workers, name='workers'),
    path('unskilled', unskilled, name='unskilled'),
    path('skilled', skilled, name='skilled'),
    path('hire/<int:user_id>/', hire, name='hire')
]
