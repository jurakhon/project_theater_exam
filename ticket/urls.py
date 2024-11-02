from django.urls import path
from .views import *

urlpatterns = [
    path('movielist/', MovieListView.as_view(), name='movie_list'),
    path('moviedetail/', MovieDetailView.as_view(), name='movie_detail'),
    path('moviecreate/',MovieCreateView.as_view(), name='movie_create'),
    path('movieupdate/<int:pk>',MovieUpdateView.as_view(), name='movie_update'),
    path('moviedelete/<int:pk>',MovieDeleteView.as_view(), name='movie_delete'),

]