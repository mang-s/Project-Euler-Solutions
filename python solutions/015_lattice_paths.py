    #
    # Solved by mang-s
    # Date: 06/04/25
    #
    # https://projecteuler.net/problem=15
    # https://github.com/mang-s/Project-Euler-Solutions
    #

    #
    # This page helped a lot for this problem: https://mathworld.wolfram.com/LatticePath.html
    #
    # "The number of paths of length a + b from the origin (0, 0) to a point (a, b) which are restricted to 
    # east and north steps is given by the binomial coefficient:
    # binom(a + b, a) = (a+b)! / a!b!"
    #

from math import factorial

    # Solution by combinatorics
    
def lattice_paths(width: int = 20, height:int = 20) -> int: # where width = a and height = b in the previous formula
    
    return factorial(width + height) // (factorial(width)*factorial(height)) # a!b! always divisible by (a+b)!
        
if __name__ == "__main__":
    
    print(lattice_paths())