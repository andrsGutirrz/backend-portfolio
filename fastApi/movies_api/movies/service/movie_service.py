"""
This class will emulate database connection
@author: Andres Gutierrez
"""
from typing import List, Dict, Optional

from thefuzz import fuzz, process

from movies.data.data import Data
from movies.models.movie import Movie
from movies.models.movie_response import MovieResponse


def safe_lower(prop: Optional[str]) -> str:
    return prop.lower() if prop else prop


def lower_list(props: List) -> List:
    return [safe_lower(prop) for prop in props]


def fuzz_search(look_up: str, choices: List) -> bool:
    """
    Using Fuzzy matching, it is going to return true if there is any coincidence with ration > 70
    :param look_up:
    :param choices:
    :return:
    """
    extracted = process.extract(look_up, choices)
    extracted_higher = [e for e in extracted if e[1] > 70]
    return bool(extracted_higher)


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
        # use fuzz comp https://github.com/seatgeek/thefuzz
        data = self.__data.get_all_movies()
        filters = {k: lower_list(v) for k, v in filters.items()}
        # If all filters are empty, then show all results
        any_active_filter = any(list(map(lambda movie: bool(movie), filters.values())))
        if not any_active_filter:
            return data

        filter_results = filter(
            lambda movie:
            fuzz_search(movie.type, filters.get("type", [])) or
            fuzz_search(movie.cast, filters.get("cast", [])) or
            fuzz_search(movie.title, filters.get("title", [])) or
            fuzz_search(movie.rating, filters.get("rating", [])) or
            fuzz_search(movie.country, filters.get("country", [])) or
            fuzz_search(movie.director, filters.get("director", [])) or
            fuzz_search(movie.duration, filters.get("duration", [])) or
            fuzz_search(movie.listed_in, filters.get("listed_in", [])) or
            fuzz_search(movie.date_added, filters.get("date_added", [])) or
            fuzz_search(movie.description, filters.get("description", [])) or
            fuzz_search(movie.release_year, filters.get("release_year", []))
            ,
            data)
        return list(filter_results)
