import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0

def bfs(road, loc, d):
    global n, m, answer

    deq = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[loc[0]][loc[1]] = True
    deq.append([loc, d, 1])
    

    while deq:
        cur, direct, cnt = deq.popleft()
        isFowarded = False
        answer = max(answer, cnt)

        for i in range(1, 5):
            nd = direct - i
            if nd < 0: nd = 4 + nd
            
            ny, nx = cur[0] + dy[nd], cur[1] + dx[nd]
            if (visited[ny][nx] == True): continue
            if (road[ny][nx] == 1): continue
            deq.append([[ny, nx], nd, cnt + 1])
            visited[ny][nx] = True
            isFowarded = True
            break
        
        if isFowarded: continue
        ny, nx = cur[0] - dy[direct], cur[1] - dx[direct]
        
        if (road[ny][nx] == 1): break
        deq.append([[ny, nx], direct, cnt])


if __name__=="__main__":
    n, m = map(int, input().split())
    *loc, d = map(int, input().split())
    road = []
    for i in range(n):
        temp = list(map(int, input().split()))
        road.append(temp)
    
    bfs(road, loc, d)

    print(answer)