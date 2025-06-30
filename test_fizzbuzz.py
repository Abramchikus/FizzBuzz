import pytest

from fizzbuzz import fizzbuzz


def test_string_return() -> None:
    result = fizzbuzz('1')
    assert isinstance(result, str)

def test_not_string_input() -> None:
    results = [
        fizzbuzz(1),
        fizzbuzz(False),
        fizzbuzz(None)
    ]

    for result in results:
        assert result == 'ERROR'


def test_empty_string_input() -> None:
    result = fizzbuzz('')
    assert result == 'ERROR'

def test_not_digits_string_input() -> None:
    result = fizzbuzz('not_number')
    assert result == 'ERROR'

def test_not_natural_string_input() -> None:
    results = [
        fizzbuzz('0'),
        fizzbuzz('1.2'),
        fizzbuzz('-5')
    ]

    for result in results:
        assert result == 'ERROR'

def test_input_number_divides_only_by_three() -> None:
    results = [
        fizzbuzz('3'),
        fizzbuzz('9'),
        fizzbuzz('33'),
        fizzbuzz('123')
    ]

    for result in results:
        assert result == 'Fizz'

def test_input_number_divides_only_by_five() -> None:
    results = [
        fizzbuzz('5'),
        fizzbuzz('10'),
        fizzbuzz('55'),
        fizzbuzz('500')
    ]

    for result in results:
        assert result == 'Buzz'

def test_input_number_divides_by_three_and_five() -> None:
    results = [
        fizzbuzz('15'),
        fizzbuzz('30'),
        fizzbuzz('75'),
        fizzbuzz('300')
    ]

    for result in results:
        assert result == 'Fizz Buzz'

def test_input_number_not_divides_by_three_and_five() -> None:
    numbers = ['1', '7', '112', '511']
    for number in numbers:
        result = fizzbuzz(number)
        assert result == number