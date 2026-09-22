    #
    # Solved by mang-s
    # Date: 03/04/25
    #
    # https://projecteuler.net/problem=4
    # https://github.com/mang-s/Project-Euler-Solutions
    #

def largest_palindrome_product(rangemax: int = 999) -> int:
    
    largest = 0
    
    for i in range(1, rangemax + 1):
        for j in range(1, rangemax + 1):
            num = i * j
            if is_palindrome(num) and num > largest:
                largest = num
    
    return largest

def is_palindrome(num: int) -> bool:
    
    return str(num) == str(num)[::-1]

if __name__ == "__main__":
    print(largest_palindrome_product())
