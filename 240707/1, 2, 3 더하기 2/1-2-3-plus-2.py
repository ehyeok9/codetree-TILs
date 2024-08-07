import sys

input = sys.stdin.readline

def dp(n):
    memo = [[0] * 4 for _ in range(n+1)]
    memo[1][1] = memo[2][2] = memo[3][1] = memo[3][2] = memo[3][3] = 1
    
    for i in range(4, n+1):
        memo[i][1] = (memo[i-1][2] + memo[i-1][3]) % 1000000007
        memo[i][2] = (memo[i-2][1] + memo[i-2][3]) % 1000000007
        memo[i][3] = (memo[i-3][1] + memo[i-3][2]) % 1000000007

    return sum(memo[n]) % 1000000007
    

if __name__=="__main__":
    n = int(input())

    print(dp(n))