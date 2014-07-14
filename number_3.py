#!/usr/bin/python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import sys

def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, (number//2)+1):
        # When i reaches more than the half, there are no more natural numbers to divide by
        if number % i == 0:
            return False
    else:
        return True

def main():
    number = 8
    for i in range(100):
        print(str(i) + ": " + str(is_prime_number(i)))
 
if __name__ == '__main__':
    sys.exit(main())
