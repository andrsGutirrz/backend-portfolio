"""
This class loads movies information from external file.
It uses Pandas Lib.
@author: Andres Gutierrez
"""
import csv
import os
from typing import List, Dict


def load_from_csv() -> List[Dict]:
    """
    Read csv file
    :return: Dictionary of MovieDto
    """
    filename = r'netflix_titles.csv'
    file_to_open = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data', filename))

    if not os.path.exists(file_to_open):
        raise FileNotFoundError(file_to_open)
    with open(file_to_open, encoding="utf8", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]
