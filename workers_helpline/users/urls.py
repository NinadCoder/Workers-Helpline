from django.urls import path
from django.contrib.auth import views as auth_views
from users import views
from django.contrib.auth.views import LogoutView
from django.views.decorators.http import require_http_methods

urlpatterns = [
    path('', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

logout_view = require_http_methods(["GET", "POST"])(LogoutView.as_view())