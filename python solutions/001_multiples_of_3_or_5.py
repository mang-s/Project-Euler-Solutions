    #
    # Solved by mang-s
    # Date: 03/04/25
    #
    # https://projecteuler.net/problem=1
    # https://github.com/mang-s/Project-Euler-Solutions
    #

def multiples_of_3_or_5(number: int = 1000) -> int:
    
    return sum(num for num in range(number) if num % 3 == 0 or num % 5 == 0)

if __name__ == "__main__":
    print(multiples_of_3_or_5())
