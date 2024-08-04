import sys

input = sys.stdin.readline

def getMaximum(red, black):
    global c, n
    
    black.sort(key = lambda x : ((x[0] + x[1])/2, x[1]), reverse = True)
    red.sort(reverse = True)
    
    answer = 0
    redIdx = 0
    # print(black)
    # print(red)
    for i in range(n):
        start, end = black[i]
        for j in range(redIdx, c):
            if start <= red[j] <= end:
                answer += 1
                redIdx = j+1
                # print(black[i], red[j], redIdx)
                break

        if redIdx == c: break

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