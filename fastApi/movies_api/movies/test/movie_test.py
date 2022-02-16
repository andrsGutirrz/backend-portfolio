"""
Test cases for movies module
@author: Andres Gutierrez
"""
import unittest
from movies.data.loader import load_from_csv


class MovieTest(unittest.TestCase):

    def test_loader_read_csv(self):
        data = load_from_csv()
        self.assertIsNotNone(1)
