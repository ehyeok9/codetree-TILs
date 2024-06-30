import sys

input = sys.stdin.readline 

if __name__=="__main__":
    n = int(input())
    if n == 1:
        print(1)
    else:
        memo = [0 for _ in range(n+1)]
        memo[1] = 1
        memo[2] = 2
        
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
            memo[i] %= 1000000007

        print((memo[n] + memo[n-1]) % 1000000007)