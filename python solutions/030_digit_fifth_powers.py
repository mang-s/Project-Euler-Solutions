    #
    # Solved by mang-s
    # Date: 22/08/25
    #
    # https://projecteuler.net/problem=30
    # https://github.com/mang-s/Project-Euler-Solutions
    #

    # The maximum value for one digit is 9^5 = 59049. We can find out the maximum possible sum for a given number of digits by 
    # multiplying 59049 with the number of digits. Let's say we're gonna check the number 123456789. That's 9 digits, so 
    # the maximum sum would be 9*59049 = 531441, which doesn't even come close to 123456789. So we know we can forget about any 
    # number 9-digit number because we'll never be able to reach a big enough sum. And it'll only get worse with larger numbers
    
    # Explanation by snq_old on the problem thread https://projecteuler.net/thread=30

def digit_fifth_power(nth_power: int = 5) -> int:
    
    valid_nums = []
    
    for number in range(2, 1000000):
        num_str = str(number)
        sum_of_powers = 0
        
        for i in num_str:
            sum_of_powers += int(i) ** nth_power
        
        if sum_of_powers == int(num_str):
            valid_nums.append(sum_of_powers)
            print(sum_of_powers)
    
    return sum(valid_nums)
    
if __name__ == "__main__":
    
    print(digit_fifth_power())