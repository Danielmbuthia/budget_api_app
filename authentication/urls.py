from django.urls import path

from .views import RegisterUsers, VerifyEmail, LoginUser

urlpatterns = [
    path('register', RegisterUsers.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('verify_email', VerifyEmail.as_view(), name='verify_email')
]
