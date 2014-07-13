"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
import sys
 
def is_multiple_of_three_or_five(number):
    return number % 3 == 0 or number % 5 == 0
   
def  sum_of_multiples(range_):
    return sum([x for x  in range(range_) if is_multiple_of_three_or_five(x)])
 
def main():
    print(sum_of_multiples(1000))    
 
if __name__ == '__main__':
    sys.exit(main())
