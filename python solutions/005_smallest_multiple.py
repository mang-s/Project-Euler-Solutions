    #
    # Solved by mang-s
    # Date: 04/04/25
    #
    # https://projecteuler.net/problem=5
    # https://github.com/mang-s/Project-Euler-Solutions
    #
    
from math import lcm

def smallest_multiple(rangemax: int = 20) -> int:
    
    # Find the lcm (least common multiple) for numbers [1, n=20] with math.lcm()
        
    return lcm(*[i for i in range(2, rangemax + 1)])
    
if __name__ == "__main__":
    print(smallest_multiple())