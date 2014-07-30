#!/usr/bin/python
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import sys


def get_factorial(n):
    i = 2
    previous = 1

    if n < 0:
        return 0  # Illegal value. Also evaluates to False

    if n == 1:
        yield 1

    while i < n+1:
        previous *= i
        yield previous
        i += 1


def sum_factorial_digits(n):
    last_factorial = max(get_factorial(n))
    # A number can be looped over if converted to string. Hence the str()
    return sum(map(int, str(last_factorial)))


def main():
    print(sum_factorial_digits(100))

if __name__ == '__main__':
    sys.exit(main())
