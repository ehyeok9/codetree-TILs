import sys

input = sys.stdin.readline

def greedy(brackets):
    global n

    brackets.sort(key = lambda x : (-x[1], -x[2], -x[3]))
    temp = [brackets[i][0] for i in range(n)]
    string = "".join(temp)
    # print(brackets)
    answer = calcAnswer(string)

    print(answer)
# 6 6 6 5 4 4 3 0
# ((()( )(( )( )))(
def calcAnswer(string):
    point = string.count(')')
    stringList = list(string)
    answer = 0

    for i in range(len(stringList)):
        if stringList[i] == '(':
            answer += point
        elif stringList[i] == ')':
            point -= 1
    
    return answer


def preprocessing(brackets):
    global n
    
    for i in range(n):
        left = brackets[i].count('(')
        right = brackets[i].count(')')
        isOnlyLeft = -1
        if right == 0: isOnlyLeft = left

        brackets[i] = [brackets[i], isOnlyLeft, left-right, left]

if __name__=="__main__":
    n = int(input())
    brackets = [
        input().strip()
        for _ in range(n)
    ]

    preprocessing(brackets)

    greedy(brackets)