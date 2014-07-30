"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import sys
from functools import reduce
from operator import mul


def product(list_):
    return reduce(mul, list_)


def get_factorial(n):
    i = 2
    previous = 1

    if n < 0:
        return 0  # Illegal value. Evaluates to none

    # Wish to yield 1 once if n is zero. Twice otherwise
    for i in range((n >= 1) + 1):  # Will be 2 if n >= 1. Else 1
        yield 1

    while i < n+1:
        previous *= i
        yield previous
        i += 1


def factorial(n):
    return product(get_factorial(n))

def main():
    print(factorial(100))

if __name__ == '__main__':
    sys.exit(main())

