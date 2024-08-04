import sys
import heapq

input = sys.stdin.readline

def getMaximum(red, black):
    global c, n
    
    heapq.heapify(red)
    black.sort()

    # print(black)
    # print(red)
    answer = 0
    blackIdx = 0
    while red:
        if blackIdx == n: break
        val = heapq.heappop(red)

        for i in range(blackIdx, n):
            start, end = black[i]
            if start <= val <= end:
                blackIdx = i+1
                answer += 1
                break

    return answer


if __name__=="__main__":
    c, n = map(int, input().split())
    red = [
        int(input())
        for _ in range(c)
    ]
    black = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    print(getMaximum(red, black))