    #
    # Solved by mang-s
    # Date: 28/04/25
    #
    # https://projecteuler.net/problem=21
    # https://github.com/mang-s/Project-Euler-Solutions
    #

def amicable_numbers(rangemax: int = 10000) -> int:
    
    amicables = [] # List of all amicable numbers under 10000
    for a in range(1, rangemax + 1):
        divisors_a = get_proper_divisors(a)
        b = d(divisors_a)
        
        divisors_b = get_proper_divisors(b)
        c = d(divisors_b)
        
        if a == c and b != a:
            amicables.append(a)
            amicables.append(b)

    return sum(i for i in set(amicables))

def get_proper_divisors(number: int) -> list:
    
    return [i for i in range(1, int(number / 2 + 1)) if number % i == 0]

def d(divisors: list) -> int:
    return sum(i for i in divisors)

if __name__ == "__main__":
    
    print(amicable_numbers())
