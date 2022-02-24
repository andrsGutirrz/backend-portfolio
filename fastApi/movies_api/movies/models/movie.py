"""
Movie Model
@author: Andres Gutierrez
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Movie:
    show_id:      Optional[str] = None
    type:         Optional[str] = None
    title:        Optional[str] = None
    director:     Optional[str] = None
    cast:         Optional[str] = None
    country:      Optional[str] = None
    date_added:   Optional[str] = None
    release_year: Optional[str] = None
    rating:       Optional[str] = None
    duration:     Optional[str] = None
    listed_in:    Optional[str] = None
    description:  Optional[str] = None
