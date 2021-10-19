from django.db import models


# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.model} {self.year}'


class Person(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name