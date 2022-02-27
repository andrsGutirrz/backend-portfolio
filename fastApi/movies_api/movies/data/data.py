"""
This class will emulate database connection
@author: Andres Gutierrez
"""
from typing import List

from movies.data.loader import load_from_csv
from movies.models.movie import Movie


def get_data() -> List[Movie]:
    raw_data = load_from_csv()
    return [
        Movie(
            type=row.get("type"),
            cast=row.get("cast"),
            title=row.get("title"),
            rating=row.get("rating"),
            show_id=row.get("show_id"),
            country=row.get("country"),
            director=row.get("director"),
            duration=row.get("duration"),
            listed_in=row.get("listed_in"),
            date_added=row.get("date_added"),
            description=row.get("description"),
            release_year=row.get("release_year")
        )
        for row in raw_data]


class Data:

    def __init__(self):
        self.movies_data = get_data()

    def get_all_movies(self) -> List[Movie]:
        return self.movies_data

    def get_movie(self):
        pass

    def update_movie(self):
        pass

    def delete_movie(self):
        pass
