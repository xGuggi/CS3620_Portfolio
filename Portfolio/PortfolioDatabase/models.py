from django.db import models


# Create your models here.

class Hobbies(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500, default="default.jpg")


class Portfolio(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500, default="default.jpg")
