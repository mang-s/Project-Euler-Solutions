    #
    # Solved by mang-s
    # Date: 22/08/25
    #
    # https://projecteuler.net/problem=27
    # https://github.com/mang-s/Project-Euler-Solutions
    #
    
    # We need to find the pair of coefficients (a, b) for which the quadratic formula n^2 + an + b 
    # produces the longest sequence of consecutive prime numbers, starting from n=0
    
    # After finding the pair (a, b) then we need to compute the product a*b and return that answer
    
import math

def quadratic_primes(a_rangemax: int = 999, b_rangemax: int = 1000) -> int:

    coefs_consecutives = dict()
    
    for a in range(-1 * a_rangemax, a_rangemax + 1):
        
        for b in range(-1 * b_rangemax, b_rangemax + 1):
            
            consecutives_a_b = how_many_consecutive_primes(a, b)
            
            if consecutives_a_b > 0:
                coefs_consecutives[(a, b)] = consecutives_a_b
            
    largest_pair = sorted(coefs_consecutives.items(), key=lambda n: n[1], reverse=True)[0]
    
    return largest_pair[0][0] * largest_pair[0][1]
    
def how_many_consecutive_primes(a: int, b: int) -> int:
    
    # Quadratic formula: n^2 + an + b 
    
    n = -1
    consecutives = True
    counter = 0
    
    while consecutives:
        n = n+1
    
        if is_prime( n**2 + a*n + b ):
            counter += 1
        else:
            consecutives = False
            
    return counter
    
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
    
    print(quadratic_primes())