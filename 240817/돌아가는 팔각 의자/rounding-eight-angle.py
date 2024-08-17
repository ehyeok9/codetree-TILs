import sys
from collections import deque

input = sys.stdin.readline

def rotateClock(deq):
    deq.appendleft(deq.pop())

def rotateReversedClock(deq):
    deq.append(deq.popleft())

def judge(leftDeq, rightDeq):
    if (leftDeq[2] != rightDeq[6]):
        return True
    return False

def executeCommand(tables, tableNum, direction, visited):
    if (tableNum < 0 or tableNum >= 4): return

    if (visited[tableNum] == True): return
    visited[tableNum] = True
    # print(tableNum, direction)
    if (tableNum == 0 and judge(tables[tableNum], tables[tableNum+1])):
        executeCommand(tables, tableNum + 1, -direction, visited)
    elif (tableNum == 3 and judge(tables[tableNum-1], tables[tableNum])):
        executeCommand(tables, tableNum - 1, -direction, visited)
    else:
        if judge(tables[tableNum-1], tables[tableNum]):
            executeCommand(tables, tableNum - 1, -direction, visited)
        if judge(tables[tableNum], tables[tableNum+1]):
            executeCommand(tables, tableNum + 1, -direction, visited)

    if (direction == 1): rotateClock(tables[tableNum])
    else: rotateReversedClock(tables[tableNum])

def calcResult(tables):
    result = 0
    for i in range(4):
        result += pow(2,i) * tables[i][0]
    return result
    

if __name__=="__main__":
    tables = []
    for i in range(4):
        tables.append(
            deque(map(int, input().strip()))
        )
    
    k = int(input())
    commands = [
        list(map(int, input().split()))
        for _ in range(k)
    ]

    for tableNum, direction in commands:
        visited = [False] * 4
        executeCommand(tables, tableNum-1, direction, visited)
        # print(tables)
    print(calcResult(tables))