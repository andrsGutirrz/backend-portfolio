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

    def test_fuzz(self):
        from thefuzz import fuzz, process
        ration = fuzz.ratio("this is a test", "this is a test!")
        print(ration)
        self.assertGreater(ration, 90)

        choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
        extracted = process.extract("new york jets", choices)
        print(extracted)
