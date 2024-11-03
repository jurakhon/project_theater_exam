from datetime import datetime
from select import select

from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_of_release = models.DateField()
    description = models.TextField()
    trailer = models.URLField()
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.name


class Theater(models.Model):
    name = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    seat_quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    show_time = models.DateTimeField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return self.name + " " + self.surname

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateField(auto_now=True)
    def __str__(self):
        return f'Name: {self.user.name} Surname: {self.user.surname} Movie: {self.movie.name} Location: {self.theater.name} Show_Time: {self.theater.show_time}'
