from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Actor(models.Model):
    full_name = models.CharField(max_length=100)
    birth_year = models.PositiveSmallIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='movies/', null=True, blank=True)

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return self.full_name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    description = models.TextField()
    views = models.PositiveIntegerField(null=True, blank=True)
    video = models.FileField(upload_to='movies/', null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor, blank=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


