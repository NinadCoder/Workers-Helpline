from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),
    path('workers/', include('workers_board.urls')),
    path('register/', include('users.urls'))
]
