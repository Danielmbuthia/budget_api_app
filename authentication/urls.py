from django.urls import path

from .views import RegisterUsers, VerifyEmail

urlpatterns = [
    path('register/', RegisterUsers.as_view(), name='register'),
    path('verify_email', VerifyEmail.as_view(), name='verify_email')
]
