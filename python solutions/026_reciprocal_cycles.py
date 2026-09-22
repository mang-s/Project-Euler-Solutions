    #
    # Solved by mang-s
    # Date: 28/05/25
    #
    # https://projecteuler.net/problem=26
    # https://github.com/mang-s/Project-Euler-Solutions
    #
    
def reciprocal_cycles(rangemax: int = 1000) -> int:
    
    fractions_length = dict() # fraction: length
    
    for fraction in range(2, rangemax):
        fractions_length[fraction] = get_cycle_length(fraction)

    return max(fractions_length.keys(), key=fractions_length.get) # max fraction (key) depending on the value
    
def get_cycle_length(fraction: int) -> int:
    
    # Remove all factors of 2 and 5 as they do not have cycles
    
    while fraction % 2 == 0:
        fraction //= 2
    while fraction % 5 == 0:
        fraction //= 5

    length = 0
    if fraction != 1:
        remainder = 10 % fraction
        length = 1
        while remainder != 1:
            remainder = (remainder * 10) % fraction
            length += 1

    return length
    
if __name__ == "__main__":
    
    print(reciprocal_cycles())