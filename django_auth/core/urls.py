from django.urls import path

from .views import LoginView, SignUpView
from core import views

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', SignUpView.as_view(), name='signup'),
]
