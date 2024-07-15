import sys

input = sys.stdin.readline

diff = float("inf")

def dfs(numbers, idxList):
    global total, s, diff

    if len(idxList) == 2:
        tsum = total - numbers[idxList[0]] - numbers[idxList[1]]
        tdiff = abs(s - tsum)
        if tdiff < diff:
            diff = tdiff
        return
    
    for i in range(len(numbers)):
        if i not in idxList:
            idxList.append(i)
            dfs(numbers, idxList)
            idxList.pop()
    

if __name__ == "__main__":
    n, s = map(int, input().split())
    numbers = list(map(int, input().split()))
    total = sum(numbers)

    dfs(numbers, [])

    print(diff)