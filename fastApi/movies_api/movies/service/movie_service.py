"""
This class will emulate database connection
@author: Andres Gutierrez
"""
from typing import List, Dict

from movies.data.data import Data
from movies.models.movie import Movie
from movies.models.movie_response import MovieResponse


class MovieService:

    def __init__(self):
        self.__data = Data()

    def get_all_movies(self) -> List[Movie]:
        return self.__data.get_all_movies()

    def get_movie(self):
        raise NotImplementedError

    def update_movie(self):
        raise NotImplementedError

    def delete_movie(self):
        raise NotImplementedError

    def get_movies(self, filters: Dict) -> MovieResponse:
        movies: List[Movie] = self.__get_movies_raw(filters)
        return MovieResponse(
            size=len(movies),
            movies=movies
        )

    def __get_movies_raw(self, filters: Dict) -> List[Movie]:
        data = self.__data.get_all_movies()

        # If all filters are empty, then show all results
        any_active_filter = any(list(map(lambda movie: bool(movie), filters.values())))
        if not any_active_filter:
            return data

        filter_results = filter(
            lambda movie:
            movie.type in filters.get("type", []) or
            movie.cast in filters.get("cast", []) or
            movie.title in filters.get("title", []) or
            movie.rating in filters.get("rating", []) or
            movie.country in filters.get("country", []) or
            movie.director in filters.get("director", []) or
            movie.duration in filters.get("duration", []) or
            movie.listed_in in filters.get("listed_in", []) or
            movie.date_added in filters.get("date_added", []) or
            movie.description in filters.get("description", []) or
            movie.release_year in filters.get("release_year", [])
            ,
            data)
        return list(filter_results)
