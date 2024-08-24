import sys
from collections import deque

input = sys.stdin.readline

global r, c, k
global forest

exit = [0, 1, 2, 3]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def setupGolem(row, colum):
    forest[row][colum], forest[row][colum - 1], forest[row][colum + 1] = [1,1,1]
    forest[row - 1][colum], forest[row + 1][colum] = [1,1]
    return (row, colum)

def eraseGolem(row, colum):
    forest[row][colum], forest[row][colum - 1], forest[row][colum + 1] = [0,0,0]
    forest[row - 1][colum], forest[row + 1][colum] = [0,0]

def initialForest():
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            forest[i][j] = 0

def check(checkList):
    for y, x in checkList:
        if (y > r+3) or not (1 <= x <= c):
            return False
        if (forest[y][x] != 0):
            return False
    return True

def isPossibleSouth(pos):
    row, col = pos
    checkList = [(row+1, col-1), (row+2, col), (row+1, col +1)]
    return check(checkList)

def moveSouth(pos):
    row, col = pos
    eraseGolem(row, col)
    return setupGolem(row+1, col)

def isPossibleWestSouth(pos):
    row, col = pos
    checkList = [(row, col-2), (row+1, col-1), (row-1, col-1), (row+1, col-2), (row+2, col-1)]
    return check(checkList)

def moveWestSouth(pos):
    row, col = pos
    eraseGolem(row, col)
    return setupGolem(row+1, col-1)

def isPossibleEastSouth(pos):
    row, col = pos
    checkList = [(row, col+2), (row+1, col+1), (row-1, col+1), (row+1, col+2), (row+2, col+1)]
    return check(checkList)

def moveEastSouth(pos):
    row, col = pos
    eraseGolem(row, col)
    return setupGolem(row+1, col+1)

def bfs(visited, row, col):
    deq = deque([(row, col)])
    maxi = row
    
    while deq:
        y, x = deq.popleft()
        maxi = max(maxi, y)
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not (4 <= ny <= r+3) or not (1 <= nx <= c): continue
            if visited[ny][nx]: continue
            if forest[ny][nx] == 0: continue
            deq.append([ny, nx])
            visited[ny][nx] = True
    
    return maxi - 3

def simulation(fairy):
    answer = 0

    for fairy in fairys:
        col, d = fairy
        pos = setupGolem(2, col)
        
        while True:
            if (isPossibleSouth(pos)):
                pos = moveSouth(pos)
            elif (isPossibleWestSouth(pos)):
                pos = moveWestSouth(pos)
                d = exit[d-1]
            elif (isPossibleEastSouth(pos)):
                pos = moveEastSouth(pos)
                d = (d+1)%4
            else:
                break
        
        y, x = pos
        if not (5 <= y <= r+3):
            initialForest()
            continue
        
        er, ec = y + dy[d], x + dx[d]
        visited = [
            [False for _ in range(c+1)]
            for _ in range(r+4)
        ]
        visited[y][x] = True
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            visited[ny][nx] = True
        answer += max(bfs(visited, er, ec), (y+1)-3)
        # print(answer)
    return answer

if __name__ == "__main__":
    r, c , k = map(int, input().split())
    forest = [
        [0 for _ in range(c+1)]
        for _ in range(r+4)
    ]
    fairys = [
        list(map(int, input().split()))
        for _ in range(k)
    ]

    print(simulation(fairys))