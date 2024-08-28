import sys

input = sys.stdin.readline

N, M, P, C, D = 0, 0, 0, 0, 0
ROUDOLPH = 9
board = []
points, isPassedOut, isOver = [], [], []

dy = [-1, 0, 1, 0, 1, 1, -1, -1]
dx = [0, 1, 0, -1, 1, -1, 1, -1]


def getDistance(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    return (r1 - r2) ** 2 + (c1 - c2) ** 2

def getSantaAndRoudolphLocs():
    roudolph = None
    santas = dict()
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == ROUDOLPH:
                roudolph = (i, j)
            elif board[i][j] != 0:
                santas[board[i][j]] = (i,j)
    
    return roudolph, santas

def getDistBetween(roudolph, santas):
    dists = []
    for Pn, loc in santas.items():
        distance = getDistance(roudolph, loc)
        dists.append([distance, loc[0], loc[1]])
    return dists

def inRange(r, c):
    if (1 <= r <= N) and (1 <= c <= N):
        return True
    return False    

def getNextPosition(source, target, limit):
    y, x = source
    mini = getDistance(source, target)
    result = None
    direct = None

    for i in range(limit):
        ny, nx = y + dy[i], x + dx[i]
        if not inRange(ny, nx): continue
        if (limit == 4) and (1 <= board[ny][nx] <= P): continue
        tempDist = getDistance(target, (ny, nx))
        if mini <= tempDist: continue
        mini = tempDist
        result = (ny, nx)
        direct = i

    return result, direct
    
def printArr():
    for i in range(1, N+1):
        print(*board[i][1:])
    print()

def crushEvent(santaLoc, direct, Pn, point, santas):
    points[Pn] += point
    isPassedOut[Pn] = True
    # 둘이 충돌한 자리
    ny, nx = santaLoc
    # 원래 그 자리에 있던 놈이 이동할 위치
    Sr, Sc = ny + dy[direct] * point, nx + dx[direct] * point
    # 원래 그 자리에 있던 놈
    # print([Pn, (Sr,Sc)])
    # 이동 할 위치가 범위 안에 있고
    if inRange(Sr, Sc):
        # 다른 놈이 또 있으면 상호작용
        if board[Sr][Sc] != 0:
            dfs(Sr + dy[direct], Sc + dx[direct], board[Sr][Sc], direct, santas)
        santas[Pn] = (Sr, Sc)
        board[Sr][Sc] = Pn
    else:
        # 범위 밖이면 이 놈은 이제 끝이지
        isOver[Pn] = True
    
def dfs(Sr, Sc, Pn, direct, santas):
    # print(Pn, (Sr, Sc))
    # 상호작용은 산타끼리 밖에 안 일어남
    if not inRange(Sr, Sc):
        isOver[Pn] = True
        return

    if board[Sr][Sc] == 0:
        board[Sr][Sc] = Pn
        santas[Pn] = (Sr, Sc)
        return

    if board[Sr][Sc] != 0:
        tPn = board[Sr][Sc]
        santas[Pn] = (Sr, Sc)
        board[Sr][Sc] = Pn
        dfs(Sr + dy[direct], Sc + dx[direct], tPn, direct, santas)
    

def rushRoudolp(roudolph, santaLoc, santas):
    by, bx = roudolph
    result, direct = getNextPosition(roudolph, santaLoc, 8)
    ny, nx = result

    if board[ny][nx] != 0:
        crushEvent((ny,nx), direct, board[ny][nx], C, santas)    

    board[by][bx] = 0
    board[ny][nx] = ROUDOLPH

    return (ny, nx)

def moveSantas(santas, roudolph):
    keys = santas.keys()

    for Pn in sorted(keys):
        if isOver[Pn]: continue
        if isPassedOut[Pn]: continue
        
        loc = santas[Pn]
        result, direct = getNextPosition(loc, roudolph, 4)
        if (result == None): continue
        
        by, bx = loc
        board[by][bx] = 0

        if result == roudolph:
            direct = (direct + 2) % 4
            crushEvent(result, direct, Pn, D, santas)
            continue

        ny, nx = result
        board[ny][nx] = Pn
        # printArr()    

def simulation():
    roudolph, santas = getSantaAndRoudolphLocs()

    dists = getDistBetween(roudolph, santas)
    dists.sort(key = lambda x : (x[0], -x[1], -x[2]))
    
    if dists == []: return
    distance, *santaLoc = dists[0]
    
    roudolph = rushRoudolp(roudolph, santaLoc, santas)
    # printArr()
    # print(santas)
    moveSantas(santas, roudolph)
    
    for i in range(1, P+1):
        if isOver[i] == False:
            points[i] += 1
    
    # print(points[1:])

if __name__ == "__main__":
    N, M, P, C, D = map(int, input().split())
    board = [
        [0 for _ in range(N+1)]
        for _ in range(N+1)
    ]
    
    Rr, Rc = map(int, input().split())
    board[Rr][Rc] = ROUDOLPH
    
    for _ in range(P):
        Pn, Sr, Sc = map(int, input().split())
        board[Sr][Sc] = Pn
    
    points = [0 for _ in range(P+1)]
    isPassedOut = [False for _ in range(P+1)]
    isOver = [False for _ in range(P+1)]
    prev = [False for _ in range(P+1)]

    # printArr()
    for _ in range(M):
        simulation()

        for i in range(P+1):
            if prev[i] == True:
                isPassedOut[i] = False

        prev = isPassedOut[:]
    
    print(*points[1:])