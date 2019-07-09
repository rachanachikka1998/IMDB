from django.contrib import admin

# Register your models here.
from ratings.models import *

admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(MovieCast)
admin.site.register(MovieRating)
