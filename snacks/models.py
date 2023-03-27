from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass


class Rabbit(models.Model):
    name = models.CharField(max_length=200)
    foods = models.ManyToManyField(to='Food', related_name='foods', blank=True)
    owner = models.ForeignKey(
        to='User', on_delete=models.CASCADE, related_name='rabbits')

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# add extraneous comment
# adding more stuff
