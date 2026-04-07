import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(StatEngine([1, 2, 3]).get_mean(), 2)

    def test_median_even(self):
        self.assertEqual(StatEngine([1, 2, 3, 4]).get_median(), 2.5)

    def test_median_odd(self):
        self.assertEqual(StatEngine([1, 2, 3]).get_median(), 2)

    def test_empty(self):
        with self.assertRaises(ValueError):
            StatEngine([])

if __name__ == "__main__":
    unittest.main()