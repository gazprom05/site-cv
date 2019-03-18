from django.db import models

# Create your models here.

class MenuCategory(models.Model):
    name = models.CharField(verbose_name='Название пункта меню', max_length=64, unique=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название ОУ', max_length=128)
    image = models.ImageField(upload_to='other_images', blank=True)
    dates = models.CharField(verbose_name='Годы работы', max_length=64)

    def __str__(self):
        return f'{self.name}, {self.category.name}'