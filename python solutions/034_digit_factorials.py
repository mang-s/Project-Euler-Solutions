    #
    # Solved by mang-s
    # Date: 22/09/26
    #
    # https://projecteuler.net/problem=34
    # https://github.com/mang-s/Project-Euler-Solutions
    #

    # Also added in a factorial calculating function with recursion, just for fun.
    # These numbers are called "factorions"
    # Learn more: https://mathworld.wolfram.com/Factorion.html

def solution(rangemax: int) -> list:
    
    mapper = dict()

    for i in range(1, 10): # calculate all factorials 0 to 9
        mapper[i] = factorial(mapper, i)[1]

    valid = set()

    for i in range(3, rangemax):
        valid.add(logic(mapper, i))

    valid.remove(None)

    return sum(valid)

def logic(mapper: dict, current_num: int):

    elements = [i for i in str(current_num)] # get the number's digits
    
    factorials = [mapper[int(i)] for i in elements]

    res = None
    if sum(factorials) == current_num:
        # If true, return the number. Else, return None
        res = current_num
    return res

def factorial(mapper: dict, num: int) -> int:
    res = 1
    
    if num not in mapper.keys(): # the factorial HAS NOT been calculated before
        
        if (num - 1) in mapper.keys(): # the factorial before this one HAS been calculated before
            mapper[num] = num * mapper[num - 1]
            res = mapper[num]
            return mapper, res

        else: # the factorial before this HAS NOT been calculated before    
            while num > 0:
                    res = factorial(mapper, num - 1)[1]
                    mapper[num] = factorial(mapper, num)
                    num = num - 1
    
    # the factorial HAS been calculated before
    mapper[num] = res
    return mapper, res

if __name__ == "__main__":
    
    print(solution(1000000))