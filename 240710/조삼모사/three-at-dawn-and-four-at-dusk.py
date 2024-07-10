import sys

input = sys.stdin.readline

answer = float("inf")

def dfs(table, visited, cnt, start):
    global n, answer
    
    if cnt == (n//2):
        total = calc(table, visited, n)
        answer = min(answer, total)
        return
    
    for i in range(start, n):
        if visited[i]: continue
        visited[i] = True
        dfs(table, visited, cnt+1, i+1)
        visited[i] = False

def calc(table, visited, n):
    morning = 0
    night = 0

    mList= []
    nList = []
    for i in range(n):
        if visited[i]: mList.append(i)
        else: nList.append(i)

    for i in range(len(mList)):
        for j in range(i, len(mList)):
            morning += table[mList[i]][mList[j]]
            morning += table[mList[j]][mList[i]]

    for i in range(len(nList)):
        for j in range(i, len(nList)):
            night += table[nList[i]][nList[j]]
            night += table[nList[j]][nList[i]]
    
    return abs(morning - night)

if __name__=="__main__":
    n = int(input())
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
    visited = [False for _ in range(n)]

    dfs(table, visited, 0, 0)

    print(answer)