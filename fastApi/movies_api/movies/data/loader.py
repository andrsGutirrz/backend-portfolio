"""
This class loads movies information from external file.
It uses Pandas Lib.
@author: Andres Gutierrez
"""
from typing import List, Dict

from pandas import read_csv


def load_from_json():
    """TODO: implement"""
    pass


def load_from_csv() -> List[Dict]:
    """
    Read csv file
    :return: Dictionary of MovieDto
    """
    file_path = r'C:\Users\asge\Documents\git_repos\backend-portfolio\fastApi\movies_api\movies\data\netflix_titles.csv'
    netflix_titles_df = read_csv(file_path)
    return netflix_titles_df.to_dict() or [{}]
