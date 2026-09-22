    #
    # Solved by mang-s
    # Date: 28/04/25
    #
    # https://projecteuler.net/problem=20
    # https://github.com/mang-s/Project-Euler-Solutions
    #
    
from math import factorial
    
def factorials_digit_sum(target: int = 100) -> int:

    return sum(int(digit) for digit in str(factorial(target)))

if __name__ == "__main__":
    
    print(factorials_digit_sum())
