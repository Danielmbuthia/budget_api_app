import uuid

from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class UserManager(BaseUserManager):
    """how to create a user and a superuser"""

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('User must have a username')
        if email is None:
            raise TypeError('User must have an email')

        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Password is required')
        if email is None:
            raise TypeError('User must have an email')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


