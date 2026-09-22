    #
    # Solved by mang-s
    # Date: 29/04/25
    #
    # https://projecteuler.net/problem=24
    # https://github.com/mang-s/Project-Euler-Solutions
    #

from itertools import permutations

def lexicographic_permutations(digits: tuple = (0,1,2,3,4,5,6,7,8,9), target: int = 1000000) -> int:
    # Get all lexicographic permutations
    # Sort them numerically
    # Get the millionth one
    
    perm = permutations(digits)
    # itertools has a function to calculate the permutations of an iterable
    
    perm = sorted(perm)
    
    return int("".join(str(i) for i in perm[target - 1]))

    # One-line solution:
    # return int("".join(str(i) for i in sorted(permutations(digits))[target - 1]))
    
if __name__ == "__main__":
    
    print(lexicographic_permutations())
