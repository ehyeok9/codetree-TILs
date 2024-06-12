def dfs(arr, visited, cur, n, point):
    # print(visited, cur, point)
    global result

    if cur > n: return
    if point > result: result = point
    
    for i in range(cur, n):
        if visited[i] == False:
            visited[i] = True
            dfs(arr, visited, i + arr[i][0], n, point + arr[i][1])
            visited[i] = False

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visited = [False for _ in range(n)]
result = -1
dfs(arr, visited, 0, n, 0)

print(result)