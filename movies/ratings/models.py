from django.db import models

from movies.ratings import genders


class Actor(models.Model):
    gender_fields = ((genders.Male.value, genders.Female.value), (genders.Female.value, genders.Female.value))

    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(choices=gender_fields, max_length=6)


class Movie(models.Model):
    title = models.CharField(max_length=150)
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor, related_name='movies')


class MovieCast(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='cast')
    cast = models.ForeignKey('Actor', on_delete=models.CASCADE, related_name='casted_in')
    role = models.CharField(max_length=100)


class MovieRating(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()
    no_of_ratings = models.IntegerField()
