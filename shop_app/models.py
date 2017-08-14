from django.db import models


class Marks(models.Model):
    name = models.CharField(verbose_name='Марка', max_length=32)
    logo = models.ImageField(verbose_name='Логотип', upload_to='logo')

    def __str__(self):
        return self.name


class Models(models.Model):
    mark = models.ForeignKey(Marks, verbose_name='Марка')
    name = models.CharField(verbose_name='Модель', max_length=32)

    def __str__(self):
        return self.name


class Series(models.Model):
    mark = models.ForeignKey(Marks, verbose_name='Марка')
    model = models.ForeignKey(Models, verbose_name='Модель')
    name = models.CharField(verbose_name='Серия', max_length=32)
    image = models.ImageField(verbose_name='Фото', upload_to='series')

    def __str__(self):
        return self.name


class Modification(models.Model):
    mark = models.ForeignKey(Marks, verbose_name='Марка')
    model = models.ForeignKey(Models, verbose_name='Модель')
    series = models.ForeignKey(Series, verbose_name='Серия')
    motor = models.CharField(verbose_name='Двигатель', max_length=32)
    body = models.CharField(verbose_name='Кузов', max_length=32)
    doors = models.PositiveIntegerField(verbose_name='Дверей')
    power = models.PositiveIntegerField(verbose_name='Мощность')
    drive = models.CharField(verbose_name='Привод', max_length=32)
    fuel = models.CharField(verbose_name='Топливо', max_length=32)
    years = models.CharField(verbose_name='Год', max_length=32)

    def __str__(self):
        return self.motor
