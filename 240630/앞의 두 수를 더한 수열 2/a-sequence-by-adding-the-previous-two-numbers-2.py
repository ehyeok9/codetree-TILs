import sys

input = sys.stdin.readline 

if __name__=="__main__":
    n = int(input())
    if n <= 2:
        print(1)
    else:
        memo = [0 for _ in range(n+1)]
        memo[1] = 1
        memo[2] = 1

        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        
        print(memo[n])