import unittest
import sys
import math
from main import get_roots
anw1 = set([0])
anw2 = set([-1, 0, 1])
anw3 = set([-math.sqrt(3), -math.sqrt(2), math.sqrt(2), math.sqrt(3)])

class TestGetRoots(unittest.TestCase):
    def test_area(self):
         self.assertEqual(set(get_roots(1, 0, 0)), anw1)
    def test_area(self):
         self.assertEqual(set(get_roots(1, -1, 0)), anw2)
    def test_area(self):
        self.assertEqual(set(get_roots(1, -5, 6)), anw3)
