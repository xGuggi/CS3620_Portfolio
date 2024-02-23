from django.db import models


# Create your models here.

class Hobbies(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500, default="https://res.cloudinary.com/dqnqbaqf9/image/upload/v1633020018/about-mckp1_df1wt4.jpg")


class Portfolio(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500, default="https://res.cloudinary.com/dqnqbaqf9/image/upload/v1633020018/about-mckp1_df1wt4.jpg")


class Contact(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=400)
    message = models.CharField(max_length=500)
