import sys

input = sys.stdin.readline

def dp(n):
    memo = [[0] * 2 for _ in range(n+1)]
    memo[0][0] = memo[1][1] = 1

    for i in range(2, n+1):
        memo[i][0] = memo[i-1][0] + memo[i-2][0]
        memo[i][1] = memo[i-1][1] + memo[i-2][1]
    
    return memo[n]

if __name__=="__main__":
    n = int(input())
    
    if n == 0:
        print("1 0")
    else:
        print(" ".join(map(str, dp(n))))