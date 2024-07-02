import sys

input = sys.stdin.readline

def dp(n):
    memo = [float("inf") for _ in range(n+1)]
    memo[1] = 0

    for i in range(2,n+1):
        if i % 3 == 0:
            memo[i] = min(memo[i//3] + 1, memo[i])
        if i % 2 == 0:
            memo[i] = min(memo[i//2] + 1, memo[i])
        
        memo[i] = min(memo[i-1] + 1, memo[i])
    # print(memo)
    return memo[n]
    

if __name__=="__main__":
    n = int(input())

    answer = dp(n)
    
    print(answer)