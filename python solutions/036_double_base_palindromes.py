    #
    # Solved by mang-s
    # Date: 07/10/26
    #
    # https://projecteuler.net/problem=35
    # https://github.com/mang-s/Project-Euler-Solutions
    #

    # Implemented with a two-way decimal-binary converter

import time

def double_base_palindromes(rangemax: int) -> int:

    result = []

    for i in range(1, rangemax + 1):
        if is_palindrome(i):
            binary = dec_bin_converter(i)
            if is_palindrome(binary):
                result.append(i)

    return sum(result)

    # one line solution with comprehension:
    # return sum([i for i in range(1, rangemax + 1) if is_palindrome(i) and is_palindrome(dec_bin_converter(i))])

def is_palindrome(number: int) -> bool:
    # checks if the given number is palindrome.

    digits = str(number)

    return digits == digits[::-1]

def dec_bin_converter(number: int, is_decimal: bool = True ) -> int:
    # Turns a number from decimal to binary and from binary to decimal.

    result = 0

    if is_decimal: # from decimal to binary
        result = int(bin(number)[2:])
    else: # from binary to decimal
        result = int(str(number), base=2)

    return result

if __name__ == "__main__":
    
    print(double_base_palindromes(rangemax = 1000000))