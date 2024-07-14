import sys

input = sys.stdin.readline

def simulation(board):
    global r, c, k
    
    if board[r][c] == k: return 0

    lenR, lenC = 3, 3
    for i in range(1, 101):
        if lenR >= lenC:
            lenR, lenC = rowCalc(board)
        else:
            lenR, lenC = colCalc(board)

        # for i in range(1, 11):
        #     print(*board[i][:11])
        if board[r][c] == k: return i

    return -1

def colCalc(board):
    lenR = -1
    lenC = 100

    for i in range(1, 101):        
        temp = dict()

        for j in range(1, 101):
            if board[j][i] == 0: continue
            temp[board[j][i]] = temp.setdefault(board[j][i], 0) + 1
        
        if bool(temp) == False:
            lenC = i-1
            break

        sorting = sorted(temp.items(), key = lambda x : (x[1], x[0]))
        length = len(sorting) * 2
        cntList = range(1, length+1, 2)
        for idx, item in zip(cntList, sorting):
            key, val = item
            board[idx][i] = key
            board[idx+1][i] = val
        
        lenR = max(lenR, length)
        if length < 100:
            for j in range(length+1, 101):
                board[j][i] = 0

    return lenR, lenC

def rowCalc(board):
    lenR = 100
    lenC = -1

    for i in range(1, 101):
        temp = dict()
        
        for j in range(1, 101):
            if board[i][j] == 0: continue
            temp[board[i][j]] = temp.setdefault(board[i][j], 0) + 1
        
        if bool(temp) == False:
            lenR = i-1
            break

        sorting = sorted(temp.items(), key = lambda x : (x[1], x[0]))
        length = len(sorting) * 2
        cntList = range(1, length+1, 2)
        for idx, item in zip(cntList, sorting):
            key, val = item
            board[i][idx] = key
            board[i][idx+1] = val
        
        
        lenC = max(lenC, length)
        if length < 100:
            for j in range(length+1, 101):
                board[i][j] = 0

    return lenR, lenC

if __name__=="__main__":
    r, c, k = map(int, input().split())
    board = [[0 for _ in range(101)] for _ in range(101)]
    for i in range(3):
        tmp = list(map(int, input().split()))
        for j in range(3):
            board[i+1][j+1] = tmp[j]

    answer = simulation(board)

    print(answer)