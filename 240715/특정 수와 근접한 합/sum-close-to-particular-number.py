import sys

input = sys.stdin.readline

maxi = float("inf")
answer = set()

def dfs(nums, idx, idxList):
    global maxi, sumation, answer
    
    if len(idxList) == 2:
        tsum = nums[idxList[0]] + nums[idxList[1]]
        answer.add(tsum)
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

    tlist = []
    for num in answer:
        tlist.append([abs(sumation - num), num])
    tlist.sort()

    print(abs(tlist[0][1] - tlist[1][1]))