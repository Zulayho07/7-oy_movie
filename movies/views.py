from django.shortcuts import render

from .models import Genre, Movie, Actor


def home(request):
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    actors = Actor.objects.all()

    context = {
        'genres': genres,
        'movies': movies,
        'actors': actors,
    }

    return render(request, 'movie/index.html', context)


def movie_detail(request, movie_id):
    genres = Genre.objects.all()
    actors = Actor.objects.all()
    movie = Movie.objects.get(pk=movie_id)

    context = {
        'movie': movie,
        'genres': genres,
        'actors': actors,
    }
    return render(request, 'movie/detail.html', context)


def movie_by_genre(request, genre_id):
    genres = Genre.objects.all()
    actors = Actor.objects.all()
    genre = Genre.objects.get(pk=genre_id)
    movies = Movie.objects.filter(genre=genre_id)
    context = {
        'genres': genres,
        'actors': actors,
        'genre': genre,
        'movies': movies,
    }
    return render(request, 'movie/movie_by_genre.html', context)


def movie_by_actor(request, actor_id):
    actors = Actor.objects.all()
    genres = Genre.objects.all()
    actor = Actor.objects.get(pk=actor_id)
    movies = Movie.objects.filter(pk=actor_id)
    context = {
        'actors': actors,
        'genres': genres,
        'actor': actor,
        'movies': movies,
    }
    return render(request, 'movie/movie_by_actor.html', context)


