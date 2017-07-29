from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import UserManager


class UserProfile(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, verbose_name=_("Nombres"))
    last_name = models.CharField(max_length=50, verbose_name=_('Apellidos'))
    photo = models.ImageField(upload_to="photos/")
    email = models.EmailField(unique=True, verbose_name=_('Correo'))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
