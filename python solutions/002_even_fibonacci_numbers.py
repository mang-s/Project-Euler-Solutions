    #
    # Solved by mang-s
    # Date: 03/04/25
    #
    # https://projecteuler.net/problem=2
    # https://github.com/mang-s/Project-Euler-Solutions
    #

def even_fibonacci_numbers(rangemax: int = 4000000) -> int:
    
    counter, na, nb = 0, 0, 1 # na = current fibonacci number. nb = next fibonacci number in the sequendce
    
    while na < rangemax:
        fib_n = na + nb
        na, nb = nb, fib_n
        
        if fib_n % 2 == 0:
            counter += fib_n
        
    return counter

if __name__ == "__main__":
    print(even_fibonacci_numbers())
