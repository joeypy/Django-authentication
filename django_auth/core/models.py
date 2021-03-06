from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('Correo electrónico'), unique=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']
