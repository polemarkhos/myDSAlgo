def climbStairs(num):
    if num <= 1:
        return 1
    
    return climbStairs(num -1) + climbStairs(num -2)

# memoize it 

def climbMemoized(num):
    memo = {}

    if num <= 1:
        return 1
    
    if num in memo:
        return memo[num]

    memo[num] = climbStairs(num - 1) + climbStairs(num - 2)
    return memo[num]

print(climbStairs(5))
print(climbMemoized(5))

# bottom up
def climbStairsBU(num):
    if num <= 1:
        return 1
    # create a list of ways to climb n steps
    # memoizing, but from the bottom up
    dp = 0 * (num+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, num+1):
        dp[i] = dp[i -1] + dp[i-2]
    return dp[num]