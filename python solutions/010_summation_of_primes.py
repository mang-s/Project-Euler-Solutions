    #
    # Solved by mang-s
    # Date: 05/04/25
    #
    # https://projecteuler.net/problem=10
    # https://github.com/mang-s/Project-Euler-Solutions
    #

import math

def summation_of_primes(number: int = 2000000) -> int:
    
    sum = 0
    
    for i in range(2, number + 1):
        if (is_prime(i)):
            sum += i
    
    return sum

def is_prime(num: int) -> bool:
    
    result = True
    
    if num < 2:
        result = False

    else:   
        for i in range(2, int(math.sqrt(num)) + 1):
            
            if num % i == 0:
                result = False
                break

    return result

if __name__ == "__main__":
    print(summation_of_primes())