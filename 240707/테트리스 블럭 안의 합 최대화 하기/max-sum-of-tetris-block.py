import sys

input = sys.stdin.readline

shapes = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [0, 1], [1, 0], [1,1]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [1, 1], [2, 2]],
    [[0, 0], [1, 0], [1, 1], [2, 0]]
]
answer = 0

#  + x 축 반전 : x, -y 를 더하자
#  + y 축 반전 : -x, y 를 더하자
def makeReverse():
    madeReverse = []
    for shape in shapes:
        reversedByX = []
        reversedByY = []
        for dy, dx in shape:
            reversedByX.append([-dy, dx])
            reversedByY.append([dy, -dx])
        madeReverse.extend([shape, reversedByX, reversedByY])
    return madeReverse

# 만들어진 좌표를 바꾸자
#  + 90 도 회전 : -x, y
#  + 180 도 회전 : y -x
#  + 270 도 회전 : x, y
#  + 360 도 회전 : y, x
def makeRotate(reversedShapes):
    total = []
    for shape in reversedShapes:
        rotate90 = []
        rotate180 = []
        rotate270 = []
        for y, x in shape:
            rotate90.append([-x, y])
            rotate180.append([y, -x])
            rotate270.append([x, y])
        total.extend([shape, rotate90, rotate180, rotate270])
    return total

def calculation(y, x, shape, board):
    global n, m, answer
    
    val = 0
    for dy, dx in shape:
        ny, nx = y + dy, x + dx
        if (ny < 0 or ny >= n) or (nx < 0 or nx >= m): return
        val += board[ny][nx]
    
    answer = max(answer, val)
        

def simulation(board):
    global n, m

    reversedShapes = makeReverse()
    totalShapes = makeRotate(reversedShapes)

    for y in range(n):
        for x in range(m):
            for shape in totalShapes:
                calculation(y, x, shape, board)
            

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    simulation(board)

    print(answer)