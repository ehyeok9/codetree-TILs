import sys

input = sys.stdin.readline

def dp(n):
    memo = [0 for _ in range(n+1)]
    memo[1] = memo[2] = memo[3] = 1

    for i in range(4, n+1):
        memo[i] = memo[i-2] + memo[i-3]

    return memo[n]

if __name__ == "__main":
    n = int(input())
    
    if n <= 3:
        print(1)
    else:
        print(dp(n))