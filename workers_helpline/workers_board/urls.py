from django.urls import path
from .views import (
    workers,
    unskilled,
    skilled,
    hire,
    worker_detail_view,
    worker_profile
)

urlpatterns = [
    path('', workers, name='workers'),
    path('unskilled', unskilled, name='unskilled'),
    path('skilled', skilled, name='skilled'),
    path('hire', hire, name='hire'),
    # Displays a single worker's details based on their user ID
    path('hire/<int:user_id>/', worker_detail_view, name='worker_detail'),
    # Worker’s personal profile (to edit their own info)
    path('worker/profile/', worker_profile, name='worker_profile'),
]