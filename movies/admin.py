from django.contrib import admin

from .models import Genre, Actor, Movie

admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)
