"""
Routing for Movie
@author: Andres Gutierrez
"""
from typing import Optional, List

from fastapi import APIRouter
from fastapi import Query

from movies.service.movie_service import MovieService

movie_service_client = MovieService()

movie_router = APIRouter(
    prefix="/movie",
    tags=["movie"],
    responses={404: {"description": "Not found"}},
)


@movie_router.get("/moviesTempo", tags=["movie"])
async def get_all():
    """
    Temp
    :return:
    """
    return movie_service_client.get_all_movies()


@movie_router.get("/movie", tags=["movie"])
async def get_movie(
        type: List[str] = Query([]),
        cast: List[str] = Query([]),
        title: List[str] = Query([]),
        rating: List[str] = Query([]),
        country: List[str] = Query([]),
        director: List[str] = Query([]),
        duration: List[str] = Query([]),
        listed_in: List[str] = Query([]),
        date_added: List[str] = Query([]),
        description: List[str] = Query([]),
        release_year: List[str] = Query([]),
):
    filters = {
        "type": type,
        "cast": cast,
        "title": title,
        "rating": rating,
        "country": country,
        "director": director,
        "duration": duration,
        "listed_in": listed_in,
        "date_added": date_added,
        "description": description,
        "release_year": release_year,
    }
    return movie_service_client.get_movies(filters=filters)
