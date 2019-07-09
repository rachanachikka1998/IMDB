from django.shortcuts import render
from django.db.models import F, OuterRef, Sum, ExpressionWrapper, FloatField, Subquery, Count

from ratings.models import MovieRating, Actor, MovieCast, Movie
from django.db.models.functions import ExtractMonth


def top_ten_avg_rating():
    avg_expression_wrapper = ExpressionWrapper(F('total_product') / (1.0 * F('total_sum')), output_field=FloatField())
    ratings = MovieRating.objects.annotate(product=F('rating') * F('no_of_ratings')).values('movie').annotate(
        total_product=Sum('product'), total_sum=Sum('no_of_ratings')).annotate(avg=avg_expression_wrapper).order_by(
        '-avg', 'movie__title')[:10]

    return ratings


def top_five_least_five_actors():
    result = Actor.objects.annotate(count=Count('movies'))
    top_five = result.order_by('-count', 'name').values('name', 'count')[:5]
    least_five = result.order_by('count', 'name').values('name', 'count')[:5]
    print("top5\n", top_five)
    print("least5\n", least_five)


def movies_released_in_star_month():
    sub = MovieCast.objects.filter(movie_id=OuterRef('pk')).annotate(count=Count('cast__birth_date__month')).values(
        'cast__birth_date__month').order_by('count', 'title')[:1]
    return Movie.objects.annotate(month=Subquery(sub)).filter(release_date__month=F('month'))


def number_movies_in_birth_month():
    sub = Movie.objects.filter(release_date__month=OuterRef('month')).values('id')
    return Actor.objects.annotate(month=ExtractMonth('birth_date')).filter(movies__in=Subquery(sub)).annotate(
        count=Count(Subquery(sub))).values('name', 'count')
