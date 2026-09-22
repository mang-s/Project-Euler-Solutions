    #
    # Solved by mang-s
    # Date: 22/08/25
    #
    # https://projecteuler.net/problem=31
    # https://github.com/mang-s/Project-Euler-Solutions
    #

    # Coins: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

    # This problem can be solved with dynamic programming.
    # Learn more: https://medium.com/@PythonicPioneer/getting-started-with-dynamic-programming-in-data-structures-and-algorithms-126c7a16775c
    
def coin_sums(target: int = 200, coins: list = [200, 100, 50, 20, 10, 5, 2, 1]) -> int:
    
    dp = dict()
    
    for i in range(0, target + 1):
        dp[i] = 0
    dp[0] = 1 # There is 1 way to make 0 coins (no coins at all). 
              # This will be the base case for all other iterations
        
    for c in coins: # Processing coins one by one ensures that we don't count permutations
        for amount in range(c, target + 1):
            # dp[amount] is the number of ways to make amount 
            # dp[amount - c] is the number of ways to make the smaller amount (amount - c)
            
            dp[amount] = dp[amount] + dp[amount - c]
    
    return dp[target]
    
if __name__ == "__main__":
    
    print(coin_sums())