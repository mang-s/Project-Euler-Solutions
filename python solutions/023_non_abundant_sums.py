    #
    # Solved by mang-s
    # Date: 28/04/25
    #
    # https://projecteuler.net/problem=23
    # https://github.com/mang-s/Project-Euler-Solutions
    #

def non_abundant_sums(rangemax: int = 28123) -> int:
    # Step 1: Get all abundant numbers in the range [12, 28123]
    # Step 2: Get all possible sums of two abundant numbers
    # Step 3: Get all the numbers in the range that aren't stored in the previous step
    # Step 4: Sum of all numbers in the previous step
    
    abundant_numbers = [number for number in range(1, rangemax + 1) if is_abundant(number)]
    
    possible_abundant_sums = get_possible_sums(abundant_numbers)
    
    non_abundant = [i for i in range(1, rangemax + 1) if i not in possible_abundant_sums]
    
    return sum(i for i in non_abundant)

def is_abundant(number: int) -> bool:
    
    return number < sum(divisor for divisor in get_proper_divisors(number))

def get_proper_divisors(number: int) -> list:
    
    return [i for i in range(1, int(number / 2 + 1)) if number % i == 0]

def get_possible_sums(numbers: list) -> set:
    
    sums = set()
    for number1 in numbers:
        for number2 in numbers:
            sums.add(number1 + number2)
    
    return sums

    # Alternative solution via comprehension
    # return set(number1 + number2 for number1 in numbers for number2 in numbers)
    
if __name__ == "__main__":
    
    print(non_abundant_sums())
