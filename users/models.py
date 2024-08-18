from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name="номер телефона", unique=True)
    birthday = models.DateTimeField(verbose_name="дата рождения")
    photo = models.ImageField(upload_to='users/%Y/%m/%d')

    def __str__(self):
        return self.username