    #
    # Solved by mang-s
    # Date: 06/04/25
    #
    # https://projecteuler.net/problem=12
    # https://github.com/mang-s/Project-Euler-Solutions
    #

    # This helped A LOT for this problem: https://web.archive.org/web/20180103053938/http://mathforum.org/library/drmath/view/55843.html

from collections import Counter

def divisible_triangular_number(divisions: int = 500) -> int:
    
    divisors = 0
    counter = 2
    current_triangular = 1
    
    while (divisors <= divisions):
        
        # Get the number of divisors of the current_triangular
        
        divisors = get_amount_divisors(current_triangular)
        
        if (divisors <= divisions):
            current_triangular += counter
            counter += 1
    
    return current_triangular

def get_amount_divisors(num: int) -> int:
    
    prime_factors = get_prime_factors(num)

    prime_factors_multiplicity = Counter(prime_factors)
    
    powers = [[factor ** i for i in range(counter + 1)] for factor, counter in prime_factors_multiplicity.items()]
    
    total_divisors = 1
    
    for aux_list in powers:
        total_divisors *= (len(aux_list))
    
    return total_divisors

def get_prime_factors(num: int) -> list:
    
    prime_factors = []
    i = 2
    
    while (i ** 2 <= num):
        if num % i == 0:
            prime_factors.append(i)
            num //= i
        else:
            i += 1
            
    if num > 1:
        prime_factors.append(num)
    
    return prime_factors

if __name__ == "__main__":
    
    print(divisible_triangular_number())