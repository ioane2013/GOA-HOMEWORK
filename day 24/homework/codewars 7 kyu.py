# 7 kyu
# https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python
# https://www.codewars.com/kata/5300901726d12b80e8000498/train/python
# https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python

#1)code:
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

#2) code:
def fizzbuzz(n):
    return [
        'FizzBuzz' if i % 15 == 0 else
        'Fizz' if i % 3 == 0 else
        'Buzz' if i % 5 == 0 else
        i
        for i in range(1, n + 1)
    ]


#3) code:
def sum_of_minimums(numbers):
    return sum(min(row) for row in numbers)