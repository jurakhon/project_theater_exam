from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.
class MovieListView(ListView):
    model = Movie
    template_name = "movie_list.html"
    context_object_name = "movie_list"

class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"
    context_object_name = "movie_detail"

class MovieCreateView(CreateView):
    model = Movie
    fields = ['name', 'genre', 'date_of_release', 'description', 'trailer','image']
    template_name = "movie_create.html"
    success_url = reverse_lazy("movie_list")

class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['name', 'genre', 'date_of_release', 'description', 'trailer','image']
    template_name = "movie_update.html"
    success_url = reverse_lazy("movie_list")

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("movie_list")

class GenreListView(ListView):
    model = Genre
    template_name = "genre_list.html"
    context_object_name = "genre_list"

class GenreDetailView(DetailView):
    model = Genre
    template_name = "genre_detail.html"
    context_object_name = "genre_detail"

class GenreCreateView(CreateView):
    model = Genre
    fields = ['name',]
    template_name = "genre_create.html"
    context_object_name = "genre_create"
    success_url = reverse_lazy("genre_list")

class GenreUpdateView(UpdateView):
    model = Genre
    fields = ['name',]
    template_name = "genre_update.html"
    context_object_name = "genre_update"
    success_url = reverse_lazy("genre_list")

class GenreDeleteView(DeleteView):
    model = Genre
    template_name = "confirm_delete.html"
    context_object_name = "genre_delete"
    success_url = reverse_lazy("genre_list")

class TheaterListView(ListView):
    model = Theater
    template_name = "theater_list.html"
    context_object_name = "theater_list"

class TheaterDetailView(DetailView):
    model = Theater
    template_name = "theater_detail.html"
    context_object_name = "theater_detail"

class TheaterCreateView(CreateView):
    model = Theater
    fields = ['name','movie','is_active','seat_quantity', 'price', 'show_time']
    template_name = "theater_create.html"
    success_url = reverse_lazy("theater_list")

class TheaterUpdateView(UpdateView):
    model = Theater
    fields = ['name','movie','is_active','seat_quantity', 'price', 'show_time']
    template_name = "theater_update.html"
    context_object_name = "theater_update"
    success_url = reverse_lazy("theater_list")

class TheaterDeleteView(DeleteView):
    model = Theater
    template_name = "confirm_delete.html"
    context_object_name = "theater_delete"
    success_url = reverse_lazy("theater_list")


class UserListView(ListView):
    model = User
    template_name = "user_view.html"
    context_object_name = "user_list"

class UserDetailView(DetailView):
    model = User
    template_name = "user_detail.html"
    context_object_name = "user_detail"

class UserCreateView(CreateView):
    model = User
    fields = ['name', 'surname', 'phone_number']
    template_name = "user_create.html"
    success_url = reverse_lazy("user_list")

class UserUpdateView(UpdateView):
    model = User
    fields = ['name', 'surname', 'phone_number']
    template_name = "user_update.html"
    success_url = reverse_lazy("user_list")

class UserDeleteView(DeleteView):
    model = User
    template_name = "confirm_delete.html"
    context_object_name = "user_delete"
    success_url = reverse_lazy("user_list")

class OrderListView(ListView):
    model = Order
    template_name = "order_list.html"
    context_object_name = "order_list"

class OrderDetailView(DetailView):
    model = Order
    template_name = "order_detail.html"
    context_object_name = "order_detail"

class OrderCreateView(CreateView):
    model = Order
    fields = ['user', 'movie','theater','quantity']
    template_name = "order_create.html"
    success_url = reverse_lazy("order_list")

class OrderUpdateView(UpdateView):
    model = Order
    fields = ['user', 'movie','theater','quantity']
    template_name = "order_update.html"
    success_url = reverse_lazy("order_list")

class OrderDeleteView(DeleteView):
    model = Order
    template_name = "confirm_delete.html"
    context_object_name = "order_delete"
    success_url = reverse_lazy("order_list")




