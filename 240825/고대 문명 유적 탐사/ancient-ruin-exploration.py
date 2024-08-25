import sys
from collections import deque

input = sys.stdin.readline

global K, M, answer
global board, parts

dy = [1,-1,0,0]
dx = [0,0,-1,1]

def rotate90(arr, row, col):
    newArr =[
        [arr[y][x] for x in range(5)]
        for y in range(5)
    ]
    
    br, bc = row -1, col -1
    for y in range(3):
        for x in range(3):
            newArr[br + y][bc + x] = arr[br + 2 - x][bc + y]
    
    return newArr

def rotate180(arr, row, col):
    temp = rotate90(arr, row, col)
    return rotate90(temp, row, col)

def rotate270(arr, row, col):
    temp = rotate180(arr, row, col)
    return rotate90(temp, row, col)

def getTreasure(arr):
    treasure = 0

    for i in range(5):
        for j in range(5):
            if (arr[i][j] != 0):
                treasure += bfs(arr, i, j)
        #     print(treasure, end= " ")
        # print()
                
    return treasure

def bfs(arr, y, x):
    deq = deque([(y,x)])
    path = set([(y,x)])
    val = arr[y][x]

    while deq:
        r, c = deq.popleft()
        
        for i in range(4):
            ny, nx = r + dy[i], c + dx[i]
            if (ny < 0 or ny >= 5) or (nx < 0 or nx >= 5): continue
            if (ny, nx) in path: continue
            if (arr[ny][nx] != val): continue
            deq.append([ny, nx])
            path.add((ny,nx))
    
    if len(path) >= 3:
        for node in path:
            r, c = node
            arr[r][c] = 0
        return len(path)
    
    return 0

def fillBoard(arr):
    for x in range(5):
        for y in range(4, -1, -1):
            if arr[y][x] == 0:
                arr[y][x] = parts.popleft()
    
rotation = [rotate90, rotate180, rotate270]

def simulation():
    global board
    
    total = 0
    selected = []

    for y in range(1, 4):
        for x in range(1, 4):
            for idx in range(3):
                temp = rotation[idx](board, y, x)
                treasure = getTreasure(temp)
                selected.append([treasure, 90 * (idx+1), x, y, temp])
    
    selected.sort(key = lambda x : (-x[0], x[1], x[2], x[3]))
    total += selected[0][0]
    board = selected[0][4]
    fillBoard(board)

    while True:
        treasure = getTreasure(board)
        if treasure == 0: break
        total += treasure
        fillBoard(board)
    
    return total

            

if __name__ == "__main__":
    K, M = map(int, input().split())
    board = [
        list(map(int, input().split()))
        for _ in range(5)
    ]
    parts = deque(list(map(int, input().split())))

    for _ in range(K):
        answer = simulation()
        if answer == 0: break
        print(answer, end=" ")