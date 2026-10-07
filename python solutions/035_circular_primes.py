    #
    # Solved by mang-s
    # Date: 07/10/26
    #
    # https://projecteuler.net/problem=35
    # https://github.com/mang-s/Project-Euler-Solutions
    #

    # Using a sieve would be much faster but this runs in ~4 seconds so it's good enough.

from math import sqrt

def circular_primes(rangemax: int) -> int:
    
    primes = [i for i in range(3, rangemax + 1, 2) if is_prime(i)] # All primes below 1 million
    primes.append(2)

    return len([i for i in primes if is_circular_prime(i)])

def is_circular_prime(number: int) -> bool:
    # returns True if the given number is a circular prime

    rotations = get_rotations(number)

    for rot in rotations:
        if not is_prime(rot):
            return False

    return True

def get_rotations(number: int) -> list:
    # returns list with all the digit rotations of the given number

    digits = str(number)
    rotations = []
    
    for i in range(len(digits)):
        rotations.append(int(digits[i:] + digits[:i]))

    return rotations

def is_prime(num: int) -> bool:
    # True if the given number is prime

    result = True
    
    if num < 2:
        result = False
    else:
        for i in range(2, int(sqrt(num)) + 1):
            
            if num % i == 0:
                result = False
                break
                
    return result

if __name__ == "__main__":
    
    print(circular_primes(rangemax = 1000000))