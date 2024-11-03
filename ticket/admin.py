from django.contrib import admin
from ticket.models import Genre, Movie, Theater, User, Order
# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Theater)
admin.site.register(User)
admin.site.register(Order)
