from django.contrib import admin

from .models import Movie

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'vote_average',
        'movie_id',
        'overview',
        'release_date',
    )


admin.site.register(Movie, MovieAdmin)
