    #
    # Solved by mang-s
    # Date: 06/04/25
    #
    # https://projecteuler.net/problem=16
    # https://github.com/mang-s/Project-Euler-Solutions
    #
    
def power_digit_sum(power: int = 1000) -> int:
      
    return sum([int(i) for i in str(2 ** power)])
        
if __name__ == "__main__":
    
    print(power_digit_sum())