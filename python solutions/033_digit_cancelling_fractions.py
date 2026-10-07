    #
    # Solved by mang-s
    # Date: 07/10/26
    #
    # https://projecteuler.net/problem=33
    # https://github.com/mang-s/Project-Euler-Solutions
    #

    # Solution using brute force.

from math import prod

def digit_cancelling_fractions(rangemax: int) -> int:

    values = [i for i in range(11, rangemax + 1)]

    curious_fracts = []

    for i in values:
        for j in values:

            if (i % 10 == 0 and j % 10 == 0) or (j >= i): # No trivial cases and numerator greater than denominator
                pass
            elif curious_fraction(numerator = i, denominator = j):
                curious_fracts.append(i / j)

    return prod(curious_fracts) # result is the product of all curious fractions 

def curious_fraction(numerator: int, denominator: int) -> bool:
    # true if the given fraction is curious (can be simplified incorrectly and give the correct value)

    num_digits = [int(i) for i in str(numerator)]
    den_digits = [int(i) for i in str(denominator)]

    for i in (0, 1): # go over numbers 0 and 1
        for j in (0, 1): 

            if (num_digits[i] == den_digits[j]):

                new_num = num_digits[(i + 1) % 2]
                new_den = den_digits[(j + 1) % 2]

                if new_den != 0:
                    if (numerator / denominator == new_num / new_den):
                        return True

    return False

if __name__ == "__main__":
    
    print(digit_cancelling_fractions(rangemax = 99)) # using only 2-digit numbers (up to 99)