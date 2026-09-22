    #
    # Solved by mang-s
    # Date: 22/08/25
    #
    # https://projecteuler.net/problem=29
    # https://github.com/mang-s/Project-Euler-Solutions
    #

def distinct_powers(a_rangemin: int = 2, a_rangemax: int = 100, b_rangemin: int = 2, b_rangemax: int = 100) -> int:
    
    powers = set()
    
    for a in range(a_rangemin, a_rangemax + 1):
        for b in range(b_rangemin, b_rangemax + 1):
            
            powers.add(a**b)
    
    return len(powers)

    # One-line solution:
    
    # return len(set( [a**b for a in range(a_rangemin, a_rangemax + 1) for b in range(b_rangemin, b_rangemax + 1)] ))
    
if __name__ == "__main__":
    
    print(distinct_powers())