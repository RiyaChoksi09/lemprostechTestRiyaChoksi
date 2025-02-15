def min_coins(coins, target):     #define function
    dp = [100] * (target + 1)   # Initialize the DP array
    dp[0] = 0    #  0 are needed to make amount 0
    
    for coin in coins:      #we have 1,5,10 coins 
        # this is compute all amount made with the coins
        for amount in range(coin, target + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    return dp[target] if dp[target] != 100 else print("there is error")     # If dp[target] is infinity, return -1 (no solution)
coins = [1,5,10]
target = 27
print("The minimum number of coins needed is:",min_coins(coins, target)) 
