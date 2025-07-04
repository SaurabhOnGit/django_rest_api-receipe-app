
"""Database models"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """manage users"""

    def create_user(self, email, password=None, **extra_fields):
        """create and save the user"""

        if not email:
            raise ValueError('User must have an valid email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, email, password=None, **extra_fields):
        """create and save the user"""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True

        user.set_password(password)
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """user in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
