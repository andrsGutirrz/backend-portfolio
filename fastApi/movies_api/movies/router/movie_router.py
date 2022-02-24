"""
Routing for Movie
@author: Andres Gutierrez
"""
from fastapi import APIRouter

movie_router = APIRouter(
    prefix="/movie",
    tags=["movie"],
    responses={404: {"description": "Not found"}},
)


@movie_router.get("/", tags=["movie"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

