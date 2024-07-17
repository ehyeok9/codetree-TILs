import sys

input = sys.stdin.readline

def simulation(gifts):
    global n, b

    totalPrice = 0
    for i in range(n):
        gifts[i].append(sum(gifts[i]))
        totalPrice += gifts[i][-1]

    gifts.sort(reverse=True, key=lambda x : x[2])
    
    answer = 0
    for i in range(n):
        curPrice = totalPrice - (gifts[i][0]//2)
        curPassed = 0
        for j in range(n):
            if curPrice <= b:
                answer = max(answer, n-j+curPassed)
                # print(i, j, curPrice, n-j)
                break
            if (i == j):
                curPassed = 1
                continue
            curPrice -= gifts[j][-1]
    # print(gifts)
    print(answer)

if __name__=="__main__":
    n, b = map(int, input().split())
    gifts = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    simulation(gifts)
    # 78
    # 8 10 15 17 17 18 -4
    # 68 17 13 81

    # 10아래가 되는 게 있어야 댐
    # 11 17 17 15 10 8
    # 33