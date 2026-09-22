    #
    # Solved by mang-s
    # Date: 22/08/25
    #
    # https://projecteuler.net/problem=28
    # https://github.com/mang-s/Project-Euler-Solutions
    #

    # Sum of all terms on the two principal diagonals of a 2n+1 X 2n+1 square spiral is given
    # by the formula a(n) = 1 + 10*n^2 + (16*n^3 + 26*n)/3

def number_spiral_diagonals(dimensions: int = 1001) -> int:
    
    # We solve for n in 2n+1 = 1001 -> n=500

    n = int( (dimensions - 1) / 2 )

    # And apply the formula a(n) = 1 + 10*n^2 + (16*n^3 + 26*n)/3

    diagonals_sum = int( 1 + 10*(n**2) + (16*(n**3) + 26*n)/3 )
    
    # Alternative solution without the previous formula:
    
    '''
    diagonals_sum = 0

    for i in range(3, 1002, 2):
        t = i ** 2
        for j in range(4):
            diagonals_sum += t - j * (i - 1)
    diagonals_sum += 1
    '''
    
    return diagonals_sum
    
if __name__ == "__main__":
    
    print(number_spiral_diagonals())