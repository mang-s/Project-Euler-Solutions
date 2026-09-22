    #
    # Solved by mang-s
    # Date: 05/04/25
    #
    # https://projecteuler.net/problem=9
    # https://github.com/mang-s/Project-Euler-Solutions
    #

def pitagorean_triplet(sum: int = 1000) -> int:
    
    # Implementation by brute force.
                
    for a in range(1, sum + 1):
        for b in range(1, sum + 1):
            c = sum - a - b
            if (a ** 2 + b ** 2 == c ** 2):
                # Solution also works if we do `a, b = b, a` (the order of a and b don't matter)
                return a * b * c
            

if __name__ == "__main__":
    print(pitagorean_triplet())