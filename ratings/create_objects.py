from ratings.dictionaries import actors, movies, movie_cast, ratings
from ratings.models import Actor, Movie, MovieCast, MovieRating


def create_all_actors():
    for actor in actors:
        Actor.objects.create(name=actor["name"], birth_date=actor["birth_date"], gender=actor["gender"])


def create_all_movies():
    for movie in movies:
        Movie.objects.create(title=movie["title"], release_date=movie["release_date"])


def create_all_movies_cast():
    for casting in movie_cast:
        movie = Movie.objects.get(title=casting["movie"])
        cast = Actor.objects.get(name=casting["cast"])

        MovieCast.objects.create(movie=movie, cast=cast,
                                 role=casting["role"])


def create_all_ratings():
    for rating in ratings:
        movie = Movie.objects.get(title=rating["movie"])
        MovieRating.objects.create(movie=movie, rating=rating["rating"], no_of_ratings=rating["number"])
