from typing import List, Optional

from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None
) -> QuerySet[Movie]:
    queryset_movie = Movie.objects.all()

    if genres_ids is not None:
        queryset_movie = queryset_movie.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset_movie = queryset_movie.filter(actors__id__in=actors_ids)

    return queryset_movie


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)

    return new_movie