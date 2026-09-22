    #
    # Solved by mang-s
    # Date: 06/04/25
    #
    # https://projecteuler.net/problem=14
    # https://github.com/mang-s/Project-Euler-Solutions
    #

from collections import defaultdict

def longest_collatz_sequence(rangemax: int = 1000000) -> int:
    
    sequences = defaultdict(int)
    
    for starter in range(1, rangemax):
        
        i = starter
        sequences[starter] += 1

        while (i > 1):
            
            if (i % 2 == 0): # Case for even numbers
                i = i // 2
            else: # Case for odd numbers
                i = i * 3 + 1
            
            sequences[starter] += 1

    longest_sequence = 1 # Amount of numbers in the sequence
    longest_starter = 1 # Starter number for the sequence
    
    for i, j in sequences.items():
        if j > longest_sequence:
            longest_starter = i
            longest_sequence = j

    return longest_starter
        
if __name__ == "__main__":
    
    print(longest_collatz_sequence())