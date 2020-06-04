from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150)
    vote_average = models.FloatField()
    movie_id = models.IntegerField()
    overview = models.TextField()
    release_date = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['movie_id']

    def __str__(self):
        return self.title
