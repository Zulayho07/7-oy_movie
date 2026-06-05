from django.urls import path

from .views import home, movie_detail, movie_by_genre, movie_by_actor

urlpatterns = [
    path('', home, name='home'),
    path('movies/<int:movie_id>', movie_detail, name='detail'),
    path('genres/<int:genre_id>', movie_by_genre, name='movie_by_genre'),
    path('actors/<int:actor_id>', movie_by_actor, name='movie_by_actor'),
]