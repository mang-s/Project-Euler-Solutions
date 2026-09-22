    #
    # Solved by mang-s
    # Date: 05/04/25
    #
    # https://projecteuler.net/problem=7
    # https://github.com/mang-s/Project-Euler-Solutions
    #

def nth_prime(nth_prime: int = 10001) -> int:
    
    # Look for the n th prime number 
       
    # Process / Annotations:
    # Keep track on which prime number we are on
    # Stablish the latest prime as the result of the function
    # Stop the loop once we reach the nth_prime
    
    primes_counter = 0
    number_counter = -1
    latest_prime = 1
    
    while (primes_counter < nth_prime):
        number_counter += 2 # skip multiples of 2 (starting value: -1)
        
        if is_prime(number_counter):
            latest_prime = number_counter
            primes_counter += 1
            
    return latest_prime

def is_prime(number: int) -> bool:
    
    result = True
    
    for i in range(2, int(number**0.5 + 1)): # prime numbers must be in range [1, ceil(sqrt(number))]
        if number % i == 0:
            result = False
    
    return result

if __name__ == "__main__":
    print(nth_prime())
