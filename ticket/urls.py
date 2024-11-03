from django.urls import path
from .views import *

urlpatterns = [
    path('movielist/', MovieListView.as_view(), name='movie_list'),
    path('moviedetail/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('moviecreate/',MovieCreateView.as_view(), name='movie_create'),
    path('movieupdate/<int:pk>',MovieUpdateView.as_view(), name='movie_update'),
    path('moviedelete/<int:pk>',MovieDeleteView.as_view(), name='movie_delete'),
    path('genrelist/', GenreListView.as_view(), name='genre_list'),
    path('genredetail/<int:pk>',GenreDetailView.as_view(), name='genre_detail'),
    path('genrecreate/',GenreCreateView.as_view(), name='genre_create'),
    path('genreupdate/<int:pk>',GenreUpdateView.as_view(), name='genre_update'),
    path('genredelete/<int:pk>',GenreDeleteView.as_view(), name='genre_delete'),
    path('theaterlist/', TheaterListView.as_view(), name='theater_list'),
    path('theaterdetail/<int:pk>',TheaterDetailView.as_view(), name='theater_detail'),
    path('theatercreate/',TheaterCreateView.as_view(), name='theater_create'),
    path('theaterupdate/<int:pk>',TheaterUpdateView.as_view(), name='theater_create'),
    path('theaterdelete/<int:pk>',TheaterDeleteView.as_view(), name='theater_delete'),
    path('userlist/', UserListView.as_view(), name='user_list'),
    path('userdetail/<int:pk>',UserDetailView.as_view(), name='user_detail'),
    path('usercreate/',UserCreateView.as_view(), name='user_create'),
    path('userupdate/<int:pk>',UserUpdateView.as_view(), name='user_update'),
    path('userdelete/<int:pk>',UserDeleteView.as_view(), name='user_delete'),
    path('orderlist/', OrderListView.as_view(), name='order_list'),
    path('orderdetail/<int:pk>',OrderDetailView.as_view(), name='order_detail'),
    path('ordercreate/',OrderCreateView.as_view(), name='order_create'),
    path('orderupdate/<int:pk>',OrderUpdateView.as_view(), name='order_update'),
    path('orderdelete/<int:pk>',OrderDeleteView.as_view(), name='order_delete'),
    path('', MovieIndexListView.as_view(), name='movie_list'),










]