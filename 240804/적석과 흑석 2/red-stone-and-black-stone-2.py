import sys
import heapq

input = sys.stdin.readline

def getMaximum(red, black):
    global c, n
    
    red.sort()
    black.sort()

    # print(black)
    # print(red)
    answer = 0
    for start, end in black:
        for val in red:
            if start <= val <= end:
                red.remove(val)
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