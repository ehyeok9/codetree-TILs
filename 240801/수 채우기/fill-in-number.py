import sys

input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    memo = [0 for _ in range(n+1)]
    memo[1] = -1

    for i in range(2, n+1):
        if i == 2 or i == 5: memo[i] = 1
        if i == 4: memo[i] = 2
        if i == 3: memo[i] = -1
        if i >= 6: 
            if memo[i-2] == -1 and memo[i-5] == -1:
                memo[i] = -1
            elif memo[i-2] == -1:
                memo[i] = memo[i-5] + 1
            elif memo[i-5] == -1:
                memo[i] = memo[i-2] + 1
            else:
                memo[i] = min(memo[i-5], memo[i-2]) + 1

    # print(memo)
    print(memo[n])