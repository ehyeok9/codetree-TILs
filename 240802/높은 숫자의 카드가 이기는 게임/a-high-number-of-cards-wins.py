import sys

input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    totalCard = set([
        num
        for num in range(1, 2*n + 1)
    ])
    bCard = set(
        int(input())
        for _ in range(n)
    )
    aCard = totalCard - bCard

    aCard = sorted(list(aCard))
    bCard = sorted(list(bCard))
    
    answer = 0
    bIdx = 0
    for aIdx in range(n):
        if aCard[aIdx] > bCard[bIdx]:
            answer += 1
            bIdx += 1

    # print(aCard, bCard)
    print(answer)