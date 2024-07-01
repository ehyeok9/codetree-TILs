import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    
    memo = [0 for _ in range(n+1)]
    memo[0] = 1

    for i in range(1, n+1):
        for j in range(i):
            memo[i] += memo[j] * memo[i-j-1]
            
    print(memo[n])