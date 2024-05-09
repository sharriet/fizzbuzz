import pytest
from models.fizzbuzz import FizzBuzz

# if multiple of 3 return fizz
def test_multiple_of_3_return_fizz():
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.input_number(3) == "fizz"

# if multiple of 5 return buzz
def test_multiple_of_5_return_buzz():
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.input_number(5) == "buzz"

# if it is not divisible by 3 or 5 return the number

# if it is divisible by 3 and 5 return fizzbuzz
def test_multiple_of_3_and_5_return_fizzbuzz():
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.input_number(15) == "fizzbuzz"

# if input is not a number, return error message