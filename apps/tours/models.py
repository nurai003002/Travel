from django.db import models

# Create your models here.
class Tour(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название Тура'
    )
    description = models.CharField(
        max_length = 255,
        verbose_name = 'Описание Тура'
    )
    date = models.DateTimeField(
        verbose_name = 'Дата Тура'
    )
    price = models.SmallIntegerField(
        verbose_name = 'Цена Тура'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

