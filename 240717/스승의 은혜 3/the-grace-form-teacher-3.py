import sys

input = sys.stdin.readline

# 시간복잡도 N^3 제한

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
        for j in range(n):
            if (i == j): continue
            if curPrice <= b:
                answer = max(answer, n-j)
            curPrice -= gifts[j][-1]
    
    print(answer)

if __name__=="__main__":
    n, b = map(int, input().split())
    gifts = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    simulation(gifts)