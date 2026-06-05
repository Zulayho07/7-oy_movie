from django.contrib import admin
from .models import Genre, Actor, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'birth_year')
    list_filter = ('birth_year',)
    search_fields = ('full_name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'genre', 'views')
    list_filter = ('year', 'genre')
    search_fields = ('title',)
    filter_horizontal = ('actors',)