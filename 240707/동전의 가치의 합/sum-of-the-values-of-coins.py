import sys

input = sys.stdin.readline

def dp(n):
    memo = [float("inf") for _ in range(n+1)]
    memo[0] = 0
    coin = [1, 2, 5, 7]

    for i in range(1, n+1):
        for price in coin:
            if i - price < 0: continue
            memo[i] = min(memo[i-price]+1, memo[i])
    
    return memo[n]

if __name__=="__main__":
    n = int(input())

    print(dp(n))