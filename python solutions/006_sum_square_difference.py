    #
    # Solved by mang-s
    # Date: 04/04/25
    #
    # https://projecteuler.net/problem=6
    # https://github.com/mang-s/Project-Euler-Solutions
    #

def sum_square_difference(rangemax: int = 100) -> int:
    
    sum_squares = 0
    sum = 0
    
    for i in range(1, rangemax + 1):
        sum_squares += i ** 2
        sum += i
    
    return sum ** 2 - sum_squares # sum = square of the sum

if __name__ == "__main__":
    print(sum_square_difference())
