import sys

input = sys.stdin.readline

def dp():
    global a, b
    
    distance = abs(a-b)
    memo = [0 for _ in range(distance+2)]
    memo[1] = 1
    
    for i in range(2, distance+2):
        for j in range(i):
            memo[i] += memo[j] * memo[i - j]
    # print(memo)
    return memo[distance+1]

if __name__=="__main__":
    a, b = map(int, input().split())

    if (a==b): print(0)
    else: print(dp())