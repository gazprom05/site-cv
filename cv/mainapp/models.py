from django.db import models

# Create your models here.

class MenuCategoryTable(models.Model):
    name = models.CharField(verbose_name='Название пункта меню', max_length=64, unique=True)

    def __str__(self):
        return self.name


class EducationTable(models.Model):
    category = models.ForeignKey(MenuCategoryTable, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название ОУ', max_length=128)
    image = models.ImageField(upload_to='education_images', blank=True)
    dates = models.CharField(verbose_name='Годы обучения', max_length=64)

    def __str__(self):
        return f'{self.name}, {self.category.name}'


class CareerTable(models.Model):
    category = models.ForeignKey(MenuCategoryTable, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Место работы', max_length=128)
    position = models.CharField(verbose_name='Должность', max_length=128)
    image = models.ImageField(upload_to='career_images', blank=True)
    dates = models.CharField(verbose_name='Стаж работы', max_length=64)

    def __str__(self):
        return f'{self.name}, {self.category.name}'


class AddEducationTable(models.Model):
    category = models.ForeignKey(MenuCategoryTable, on_delete=models.CASCADE)
    description = models.CharField(verbose_name='Описание курсов', max_length=256)
    image = models.ImageField(upload_to='add_education_images', blank=True)
    dates = models.CharField(verbose_name='Год обучения', max_length=64)

    def __str__(self):
        return f'{self.description}, {self.category.name}'


class CertificatesTable(models.Model):
    category = models.ForeignKey(MenuCategoryTable, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название курса', max_length=128)
    image = models.ImageField(upload_to='certificate_images', blank=True)

    def __str__(self):
        return f'{self.name}, {self.category.name}'