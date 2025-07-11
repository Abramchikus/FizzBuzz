# FizzBuzz

## О проекте
Это учебная реализация FizzBuzz, созданная для практики **Test-Driven Development (TDD)**.

## Функционал
Функция ```fizzbuzz(string: str) -> str``` реализует правила детской игры с аналогичным названием.

Правила:
- При получении числа кратного 3 функция возвращает 'Fizz'.
- При получении числа кратного 5 функция возвращает 'Buzz'.
- При кратности 3 и 5 одновременно - 'Fizz Buzz'
- При получение другого натурального числа возращается исходная строка.
- В иных случаях - строка 'ERROR'.


## Примеры

```python
fizzbuzz('1') -> '1'
fizzbuzz('255') -> 'Fizz Buzz'
fizzbuzz('3') -> 'Fizz'
fizzbuzz('25') -> 'Buzz'
fizzbuzz('abc') -> 'ERROR'
fizzbuzz('-1') -> 'ERROR'
```