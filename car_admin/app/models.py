from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='марка')
    model = models.CharField(max_length=50, verbose_name='модель')

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'автомобили'


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='автомобиль')
    title = models.CharField(max_length=100, verbose_name='заголовок статьи')
    text = models.TextField(verbose_name='текст обзора')

    def __str__(self):
        return str(self.car) + ' ' + self.title

    class Meta:
        verbose_name = 'обзор'
        verbose_name_plural = 'обзоры'
