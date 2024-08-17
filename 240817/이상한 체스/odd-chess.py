import sys
from itertools import product

input = sys.stdin.readline 

global n, m
global directions, rotation, board
    

def findMax(locations, cases):
    result = 0

    for direct in cases:
        temp = 0
        visited = [[False for _ in range(m)] for _ in range(n)]
        for loc in locations:
            temp += getArea(loc, direct, visited)
        result = max(result, temp)
        
    print(result - len(locations))
    
def getArea(loc, direct, visited):
    horeseNum, y, x = loc
    area = 0

    if (horeseNum == 5):
        for move in directions[horeseNum]:
            area += paint(visited, move, y, x)
    else:
        multiply = rotation[direct[horeseNum - 1]]
        for move in directions[horeseNum]:
            move = [move[0] * multiply[0], move[1] * multiply[1]]
            area += paint(visited, move, y, x)
    
    return area

def paint(visited, move, y, x):
    dy, dx = move
    
    count = 0
    while ((0 <= y < n) and (0 <= x < m)):
        if (board[y][x] >= 6): break
        if (visited[y][x] == False):
            visited[y][x] = True
            count += 1
        y += dy
        x += dx
    return count
        

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    

    directions = [
        0,
        [[-1, 0]],
        [[0, -1], [0, 1]],
        [[-1, 0], [0, 1]],
        [[-1, 0], [0, -1], [0, 1]],
        [[-1, 0], [1, 0],[0, -1], [0, 1]],
    ]

    locations = []
    for i in range(n):
        for j in range(m):
            if 1 <= board[i][j] <= 5:
                locations.append([board[i][j], i, j])
    locations.sort(reverse=True)

    rotation = [[1,1], [-1,-1], [-1,1], [1,-1]]
    
    temp = [[0,1,2,3] for _ in range(4)]
    cases = list(product(*temp))

    findMax(locations, cases)