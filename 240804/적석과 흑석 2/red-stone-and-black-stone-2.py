import sys

input = sys.stdin.readline

def getMaximum(red, black):
    global c, n
    
    black.sort(key = lambda x : (-x[1],-x[0]))
    red.sort(reverse = True)
    
    # print(black)
    # print(red)
    answer = 0
    redIdx = 0
    for i in range(n):
        start, end = black[i]
        for j in range(redIdx, c):
            if start <= red[j] <= end:
                answer += 1
                redIdx = j+1
                # print(black[i], red[j], redIdx)
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