import unittest
from scripts.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_returns_1_for_1(self):
        i = 1
        assert fizzbuzz(i) == i
        
