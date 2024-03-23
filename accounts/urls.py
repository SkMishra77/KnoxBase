# urls.py
from django.urls import path

from .views import LoginView, RegisterView, LogoutView, LogoutAllView

urlpatterns = [
    path('auth/login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logoutall/', LogoutAllView.as_view()),
    path('register/', RegisterView.as_view()),
]
