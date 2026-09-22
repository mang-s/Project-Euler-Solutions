    #
    # Solved by mang-s
    # Date: 29/04/25
    #
    # https://projecteuler.net/problem=25
    # https://github.com/mang-s/Project-Euler-Solutions
    #
    
def thousand_digit_fib_number(target: int = 1000) -> int:
    
    solution = 0
    a, b = 0, 1
    counter = 1
    while (len(str(solution)) < target):
        solution = a + b
        a, b = b, solution
        counter += 1
    
    return counter
    
if __name__ == "__main__":
    
    print(thousand_digit_fib_number())
