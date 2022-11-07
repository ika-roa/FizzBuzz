import unittest
from scripts.fizzbuzz import calculate_fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_returns_1_for_1(self):
        i = 1
        assert calculate_fizzbuzz(i) == i

    def test_fizzbuzz_returns_2_for_2(self):
        i = 2
        assert calculate_fizzbuzz(i) == i

    def test_fizzbuzz_returns_fizz_for_3(self):
        i = 3
        assert calculate_fizzbuzz(i) == "Fizz"

    def test_fizzbuzz_returns_4_for_4(self):
        i = 4
        assert calculate_fizzbuzz(i) == i

    def test_fizzbuzz_returns_buzz_for_5(self):
        i = 5
        assert calculate_fizzbuzz(i) == "Buzz"

    def test_fizzbuzz_returns_fizzbuzz_for_15(self):
        i = 15
        assert calculate_fizzbuzz(i) == "FizzBuzz"

