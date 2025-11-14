coins = [1, 4, 5]
def solve(num):
    if num < 0:
        return 0
    if num == 0:
        return 0
    best = float('inf')
    for c in coins:
        best = min(best, solve(num - c)+1)
    return best

print(solve(15))

# memoized

num = 15
ready = [0 for i in range(20)]
value = [0 for i in range(20)]
def solveMemoized(num):
    if num < 0:
        return 0
    if num == 0:
        return 0
    if num in ready: 
        return value[num]
    best = float('inf')
    for c in coins:
        best = min(best, solve(num - c)+1)
    value[num] = best
    ready[num] = True
    return best

print(solveMemoized(num))