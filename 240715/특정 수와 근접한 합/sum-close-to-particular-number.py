import sys

input = sys.stdin.readline

cases = set()

def dfs(numbers, idxList):
    global total

    if len(idxList) == 2:
        cases.add(total - idxList[0] - idxList[1])
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

    tList = []
    for tsum in cases:
        tList.append([abs(total - tsum), tsum])
    tList.sort()

    print(abs(tList[0][1] - tList[1][1]))