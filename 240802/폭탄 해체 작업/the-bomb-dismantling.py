import sys
from functools import cmp_to_key

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    score = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    visit = [0 for _ in range(10001)]

    score.sort(key= lambda x : (-x[0],x[1]))
    
    answer = 0
    for i in range(n):
        point, lh = score[i]
        extra = sum(visit[:i+2])
        if extra <= lh:
            answer += point
            visit[lh] += 1
    
    print(answer)