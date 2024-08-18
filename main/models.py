from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Rubric(models.Model):
    super_rubric = models.ForeignKey('SuperRubric', on_delete=models.PROTECT)
    name = models.CharField(max_length=50, verbose_name='Рубрика')



class Bboard(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена', default=0)
    image = models.ImageField(verbose_name='Фотография')
    contacts = models.TextField(verbose_name='Контакты')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить в списке?')

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at',]