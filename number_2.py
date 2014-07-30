#!/usr/bin/python

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import sys
 
def get_fibonacci(last_fibonacci):
    previous_fibonacci = 0
    current_fibonacci = 1
    while True:
        (previous_fibonacci, current_fibonacci) = (current_fibonacci, current_fibonacci + previous_fibonacci)
        yield current_fibonacci
        if current_fibonacci >= last_fibonacci:
            return
 
def is_even(number):
    return number % 2 == 0
 
def sum_even_fibonacci(last_fibonacci):
    list_of_even_fibonacci = [x for x in get_fibonacci(last_fibonacci) if is_even(x)]
    return sum(list_of_even_fibonacci)
 
def main():
    """ Main entry point for script."""
    last_fibonacci = 4000000
    print(sum_even_fibonacci(last_fibonacci))
 
if __name__ == '__main__':
    sys.exit(main())
