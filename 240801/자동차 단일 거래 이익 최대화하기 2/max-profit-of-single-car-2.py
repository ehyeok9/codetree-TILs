import sys

input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    price = list(map(int, input().split()))

    answer = 0
    minVal = price[0]
    for i in range(2, n):
        if price[i] < minVal:
            minVal = price[i]
            continue
        
        tmp = price[i] - minVal
        answer = max(answer, tmp)

    print(answer)