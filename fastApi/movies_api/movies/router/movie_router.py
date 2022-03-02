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


@movie_router.get("/movie", tags=["movie"])
async def get_movie(
        type: List[str] = Query([], title='Type', description='Search by Movie Type'),
        cast: List[str] = Query([], title='Casting', description='Search by Casting'),
        title: List[str] = Query([], title='Movie Title', description='Search by Movie Title'),
        rating: List[str] = Query([], title='Rating', description='Search by Rating'),
        country: List[str] = Query([], title='Country', description='Search by Country'),
        director: List[str] = Query([], title='Director', description='Search by Director'),
        duration: List[str] = Query([], title='Duration', description='Search by Duration'),
        listed_in: List[str] = Query([], title='Listed In', description='Search by Listen In'),
        date_added: List[str] = Query([], title='Date Added', description='Search by Date Added'),
        description: List[str] = Query([], title='Movie Description', description='Search by Movie Description'),
        release_year: List[str] = Query([], title='Release Year', description='Search by Release Year')
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
