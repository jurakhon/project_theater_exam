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
    fields = "__all__"
    template_name = "movie_create.html"
    success_url = reverse_lazy("movie_list")

class MovieUpdateView(UpdateView):
    model = Movie
    fields = "__all__"
    template_name = "movie_update.html"
    success_url = reverse_lazy("movie_list")

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("movie_list")


