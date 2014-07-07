import sys
 
def is_multiple_of_three_or_five(number):
    return number % 3 == 0 or number % 5 == 0
   
def  sum_of_multiples(range_):
    return sum([x for x  in range(range_) if is_multiple_of_three_or_five(x)])
 
def main():
    print(sum_of_multiples(1000))    
 
if __name__ == '__main__':
    sys.exit(main())
