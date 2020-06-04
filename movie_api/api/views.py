from movies.models import Movie

from .serializers import MovieSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

import requests


api_key = '68867f532bce87cde2cdbbf9916cce59'
company_id = '10342'


def get_movies(comp_id=company_id, page=1, language='en'):
    """
    Получает список фильмов со стороннего API
    :param comp_id:
    :param page:
    :param language:
    :return:
    """
    payload = {'api_key': api_key, 'language': language, 'with_companies': comp_id, 'page': page}
    movies = requests.get('https://api.themoviedb.org/3/discover/movie', params=payload)

    return movies.json()


def add_fields(movies):
    """
    Вставляет поля из локальной БД в соответствующие объекты, полученные со стороннего API
    :return:
    """
    for movie in movies['results']:
        try:
            local_movie = Movie.objects.get(movie_id=movie['id'])
        except Movie.DoesNotExist:
            local_movie = None

        if local_movie:
            print(local_movie.title)
            movie['title_rus'] = local_movie.title
            movie['overview_rus'] = local_movie.overview


class MovieList(APIView):
    """
    Реализация API
    """
    def get(self, request, page):
        # movie_serializer = MovieSerializer(Movie.objects.all(), many=True)

        en_movies = get_movies(page=page)

        add_fields(en_movies)
        return Response(en_movies)
