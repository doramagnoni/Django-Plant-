from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', auth_views.SignUpView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]