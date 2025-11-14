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