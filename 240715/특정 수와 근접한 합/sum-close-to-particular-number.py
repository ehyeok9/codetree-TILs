import sys

input = sys.stdin.readline

maxi = float("inf")
answer = None

def dfs(nums, idx, idxList):
    global maxi, sumation, answer
    
    if len(idxList) == 2:
        temp = sumation - idxList[0] - idxList[1]
        if temp < maxi:
            answer = abs(idxList[0] - idxList[1])
            maxi = temp
        return

        
    for i in range(len(nums)):
        if i not in idxList:
            idxList.append(i)
            dfs(nums, i, idxList)
            idxList.pop()

if __name__ =="__main__":
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    sumation = sum(nums)

    dfs(nums, 0, [])

    print(answer)