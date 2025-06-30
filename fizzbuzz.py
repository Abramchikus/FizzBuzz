def fizzbuzz(string: str) -> str:

    if not isinstance(string, str) or not string or not string.isdecimal() or string[0] == '0':
        return 'ERROR'

    number = int(string)
    if number % 15 == 0:
        return 'Fizz Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'

    return string