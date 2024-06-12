def dfs(arr, visited, cur, n, point):
    global result
    if point > result:
        result = point
    
    for i in range(cur, n):
        if visited[i] == False:
            nxt = cur + arr[i][0]
            if nxt >= n: continue
            visited[i] = True
            dfs(arr, visited, nxt, n, point + arr[i][1])
            visited[i] = False
    


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visited = [False for _ in range(n)]
result = -1
dfs(arr, visited, 0, n, 0)
print(result)