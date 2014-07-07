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
    sys.exit(main()
