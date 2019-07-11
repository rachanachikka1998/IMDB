from django.shortcuts import render
from django.db.models import F, OuterRef, Sum, ExpressionWrapper, FloatField, Subquery, Count, Q, Func, Avg

from ratings.models import MovieRating, Actor, MovieCast, Movie
from django.db.models.functions import ExtractMonth
from django.db import models


def top_ten_avg_rating():
    avg_expression_wrapper = ExpressionWrapper(F('total_product') / (1.0 * F('total_sum')), output_field=FloatField())
    ratings = MovieRating.objects.annotate(product=F('rating') * F('no_of_ratings')).values('movie').annotate(
              total_product=Sum('product'), total_sum=Sum('no_of_ratings')). \
              annotate(avg=avg_expression_wrapper).order_by('-avg', 'movie__title')[:10]

    return ratings


def top_five_least_five_actors():
    result = Actor.objects.annotate(count=Count('movies'))
    top_five = result.order_by('-count', 'name').values('name', 'count')[:5]
    least_five = result.order_by('count', 'name').values('name', 'count')[:5]
    print("top5\n", top_five)
    print("least5\n", least_five)


def movies_released_in_star_month():
    sub = MovieCast.objects.filter(movie_id=OuterRef('pk')).annotate(count=Count('cast__birth_date__month')).values(
        'cast__birth_date__month').order_by('-count', 'title')[:1]
    return Movie.objects.annotate(month=Subquery(sub)).filter(release_date__month=F('month'))


def number_movies_in_birth_month():
    sub = Movie.objects.filter(release_date__month=OuterRef('month')).values('id')
    return Actor.objects.annotate(month=ExtractMonth('birth_date')).annotate(
        count=Count(Subquery(sub))).filter(~Q(count=0)).values('name', 'count')


def diff_between_five_and_one_stars():
    result = Actor.objects.annotate(
        five_star=Sum('movies__ratings__no_of_ratings', filter=Q(movies__ratings__rating=5))). \
        annotate(one_star=Sum('movies__ratings__no_of_ratings', filter=Q(movies__ratings__rating=1))). \
        annotate(diff=Func(F('five_star') - F('one_star'), function='ABS')). \
        values('name', 'diff').filter(~Q(diff=None)).order_by('-diff', 'name')
    return result


def most_number_of_cast_movies():
    result = Actor.objects.filter(~Q(movies__release_date__year=None)). \
                 annotate(count=Count('name', distinct=True)).values('movies__release_date__year'). \
                 annotate(no_of_actors=Count('movies__release_date__year')).values(
                 'movies__release_date__year').order_by('-count')[:1]
    return result


def order_movies_in_increasing_age_of_youngest_cast():
    from django.db.models import OuterRef

    age_expression_wrapper = ExpressionWrapper(F('release_date') - F('actors__birth_date'),
                                               output_field=models.DurationField())
    sub = Movie.objects.filter(id=OuterRef('pk')).values('id').annotate(age=age_expression_wrapper).values(
        'age').order_by('age')[:1]
    result = Movie.objects.annotate(youngest=Subquery(sub)).values('title').order_by('youngest', 'title')
    return result


def top_five_youngest_average_cast():
    age_expression_wrapper = ExpressionWrapper(F('release_date') - F('actors__birth_date'),
                                               output_field=models.DurationField())

    sub = Movie.objects.filter(id=OuterRef('pk')).values('id').annotate(avg=Avg(age_expression_wrapper)).values('avg')
    top_five = Movie.objects.annotate(avg=Subquery(sub)).order_by('avg', 'title').values('title')[:5]

    return top_five


def least_five_youngest_average_cast():
    age_expression_wrapper = ExpressionWrapper(F('release_date') - F('actors__birth_date'),
                                               output_field=models.DurationField())

    sub = Movie.objects.filter(id=OuterRef('pk')).values('id').annotate(avg=Avg(age_expression_wrapper)).values('avg')
    least_five = Movie.objects.annotate(avg=Subquery(sub)).order_by('-avg', 'title').values('title')[:5]

    return least_five


def twin_star():
    result = MovieCast.objects.annotate(actor2=F('movie__cast__cast_id')). \
                 filter(cast_id__gt=F('actor2')).values('cast', 'actor2'). \
                 annotate(count=Count('id')).order_by('-count')[:1]
    return result
