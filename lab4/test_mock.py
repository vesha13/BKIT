import unittest
from main import get_roots
from unittest.mock import patch, Mock

anw1 = set([0])
anw2 = set([-1, 0, 1])
class TestGetRoots(unittest.TestCase):
    @patch('main.get_roots', return_value = [0])
    def test(self, anw1):
        self.assertEqual(set(get_roots(1, 0, 0)), set([0]))

    @patch('main.get_roots', return_value= [-1, 0, 1])
    def test(self, anw2):
        self.assertEqual(set(get_roots(1, -1, 0)), set([-1, 0, 1]))
