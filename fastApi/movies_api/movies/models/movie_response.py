"""
Response model when requesting movies
@author: Andres Gutierrez
"""
from dataclasses import dataclass, field
from typing import Optional, List

from movies.models.movie import Movie


@dataclass
class MovieResponse:
    size: Optional[int] = 0
    movies: List[Movie] = field(default_factory=list)
