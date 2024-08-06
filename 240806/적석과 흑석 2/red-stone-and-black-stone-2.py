import sys
from sortedcontainers import SortedSet

input = sys.stdin.readline

def greedy(T, AB):
    global c, n

    AB.sort(key = lambda x : x[1])
    T.sort()

    answer = 0
    for black in AB:
        start, end = black
        val = None
        for num in T:
            if start <= num:
                val = num
                break

        if val == None: continue
        if start <= val <= end:
            answer += 1
            T.remove(val)
            # print(start, val, end)
    
    print(answer)

if __name__=="__main__":
    c, n = map(int, input().split())
    T = [
        int(input())
        for _ in range(c)
    ]
    AB = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    greedy(T, AB)