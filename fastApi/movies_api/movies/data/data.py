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
            show_id=row.get("show_id"),
            type=row.get("type"),
            title=row.get("title"),
            director=row.get("director"),
            cast=row.get("cast"),
            country=row.get("country"),
            date_added=row.get("date_added"),
            release_year=row.get("release_year"),
            rating=row.get("rating"),
            duration=row.get("duration"),
            listed_in=row.get("listed_in"),
            description=row.get("description")
        )
        for row in raw_data]


class Data:

    def __init__(self):
        self.movies_data = get_data()

    def get_all_movies(self):
        pass

    def get_movie(self):
        pass

    def update_movie(self):
        pass

    def delete_movie(self):
        pass
