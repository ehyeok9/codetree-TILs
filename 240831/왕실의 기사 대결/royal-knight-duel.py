import sys

input = sys.stdin.readline

global L, N, Q
global board, knightArea, knightScore, isDisappear, damage

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def getNextArea(i, d):
    nxtArea = knightArea.get(i)
    temp = []
    for i in range(len(nxtArea)):
        r, c = nxtArea[i]
        temp.append([r + dy[d], c + dx[d]])
    return temp

def isCanMove(area):
    for loc in area:
        y, x = loc
        if (y < 1 or y > L) or (x < 1 or x > L): return False
        if (board[y][x] == 2): return False
    return True

def checkArea(a, b):
    a = list(map(lambda x : (x[0],x[1]), a))
    b = list(map(lambda x : (x[0],x[1]), b))
    
    return (set(a) & set(b)) == set()

def move(i, d, isPossible, moveList):
    nextArea = getNextArea(i, d)
    moveList[i] = nextArea
    if not (isCanMove(nextArea)):
        isPossible.append(False)
        return

    for knight in knightArea.keys():
        if knight == i: continue
        if knight in moveList.keys(): continue
        if isDisappear[knight]: continue
        otherNextArea = knightArea[knight]
        
        if not checkArea(nextArea, otherNextArea):
            isPossible.append(True)
            move(knight, d, isPossible, moveList)

def getDamage(area):
    damage = 0
    for y,x in area:
        if board[y][x] == 1:
            damage += 1
    return damage

def simulation(i, d):
    # 기사 이동
    isPossible = []
    moveList = dict()

    move(i, d, isPossible, moveList)

    if False in isPossible:
        return
    
    for knight in moveList.keys():
        knightArea[knight] = moveList[knight]
    
    # 대결 데미지
    for knight in moveList.keys():
        if knight == i: continue
        if isDisappear[knight]: continue
        area = knightArea[knight]
        dmg = getDamage(area)
        damage[knight] += dmg
        
        if (damage[knight] >= knightScore[knight]):
            isDisappear[knight] = True

def getAnswer():
    answer = 0

    for i in range(1, N+1):
        if isDisappear[i]: continue
        answer += damage[i]
    
    return answer
    
if __name__ == "__main__":
    L, N, Q = map(int, input().split())
    answer = 0
    
    board = [
        [0] + list(map(int, input().split()))
        for _ in range(L)
    ]
    board.insert(0, [0 for _ in range(L+1)])
    
    knightArea = dict()
    knightScore = dict()
    damage = dict()
    for i in range(1, N+1):
        r, c, h, w, k = map(int, input().split())
        knightScore[i] = k
        knightArea[i] = []
        damage[i] = 0
        for y in range(h):
            for x in range(w):
                knightArea[i].append([r+y, c+x])
    
    isDisappear = [False for _ in range(N+1)]
    for _ in range(Q):
        i, d = map(int, input().split())
        if (isDisappear[i]): continue
        simulation(i, d)
    
    print(getAnswer())