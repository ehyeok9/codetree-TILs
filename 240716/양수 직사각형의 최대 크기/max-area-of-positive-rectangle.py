import sys

input = sys.stdin.readline


def bruteForce(board):
    global n, m

    answer = -1

    for y in range(n):
        for x in range(m):
            size = simulation(y,x, board)
            answer = max(answer, size)
        #     print(size, end =" ")
        # print()
    
    return answer
            
def simulation(y,x, board):
    global n, m

    temp = 0
    height = n
    
    for j in range(x, m):
        if board[y][j] < 0: break
        for i in range(y, height):
            if board[i][j] < 0:
                height = i
                break
            temp = max(temp, (j-x+1) * (i-y+1))

    return temp

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    print(bruteForce(board))