import sys
from functools import cmp_to_key

input = sys.stdin.readline

def compare(x, y):
    if x[1] < y[1]:
        return -1
    elif x[1] > y[1]:
        return 1
    else:
        if x[0] > y[0]:
            return -1
        else:
            return 1

if __name__ == "__main__":
    n = int(input())
    score = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    score.sort(cmp_to_key(compare))
    
    answer = score[0][0]
    prev = score[0][1]
    for i in range(1, n):
        point, limit = score[i]
        if prev == limit: continue
        answer += point
        prev = limit

    print(answer)