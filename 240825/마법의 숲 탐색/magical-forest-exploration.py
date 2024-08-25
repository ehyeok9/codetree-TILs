import sys
from collections import deque

input = sys.stdin.readline

global r, c, k
global forest

exit = [0, 1, 2, 3]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def setupGolem(row, colum, count):
    forest[row][colum], forest[row][colum - 1], forest[row][colum + 1] = [count] * 3 
    forest[row - 1][colum], forest[row + 1][colum] = [count] * 2
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

def moveSouth(pos, count):
    row, col = pos
    eraseGolem(row, col)
    return setupGolem(row+1, col, count)

def isPossibleWestSouth(pos):
    row, col = pos
    checkList = [(row, col-2), (row+1, col-1), (row-1, col-1), (row+1, col-2), (row+2, col-1)]
    return check(checkList)

def moveWestSouth(pos, count):
    row, col = pos
    eraseGolem(row, col)
    return setupGolem(row+1, col-1, count)

def isPossibleEastSouth(pos):
    row, col = pos
    checkList = [(row, col+2), (row+1, col+1), (row-1, col+1), (row+1, col+2), (row+2, col+1)]
    return check(checkList)

def moveEastSouth(pos, count):
    row, col = pos
    eraseGolem(row, col)
    return setupGolem(row+1, col+1, count)

def bfs(golems, row, col):
    deq = deque([(row, col)])
    visited = [
        [0 for _ in range(c+1)]
        for _ in range(r+4)
    ]
    maxi = row
    
    while deq:
        y, x = deq.popleft()
        maxi = max(maxi, y)
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not (4 <= ny <= r+3) or not (1 <= nx <= c): continue
            if visited[ny][nx]: continue
            if forest[ny][nx] == 0: continue
            if forest[ny][nx] != forest[y][x]:
                ty, tx = golems[forest[y][x]]
                if (ty != y) or (tx != x): continue
            deq.append([ny, nx])
            visited[ny][nx] = True
    
    return maxi - 3

def simulation(fairy):
    answer = 0
    count = 1
    golems = dict()

    for fairy in fairys:
        col, d = fairy
        pos = setupGolem(2, col, count)
    
        while True:
            if (isPossibleSouth(pos)):
                pos = moveSouth(pos, count)
            elif (isPossibleWestSouth(pos)):
                pos = moveWestSouth(pos, count)
                d = exit[d-1]
            elif (isPossibleEastSouth(pos)):
                pos = moveEastSouth(pos, count)
                d = (d+1)%4
            else:
                break
        
        y, x = pos
        if not (5 <= y < r+3):
            initialForest()
            count = 1
            golems = dict()
            continue

        er, ec = y + dy[d], x + dx[d]
        golems[count] = [er, ec]        
        count += 1

        answer += bfs(golems, er, ec)
        # print(answer)
        # for line in forest:
        #     print(*line)
        
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