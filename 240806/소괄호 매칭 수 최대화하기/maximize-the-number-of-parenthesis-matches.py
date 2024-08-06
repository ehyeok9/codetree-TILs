import sys
from functools import cmp_to_key

input = sys.stdin.readline

def compare(x, y):
    string1, open1, closed1 = x
    string2, open2, closed2 = y

    if open1 * closed2 < open2 * closed1:
        return 1
    if open1 * closed2 > open2 * closed1:
        return -1
    return 0

def greedy(brackets):
    global n

    brackets.sort(cmp_to_key(compare))
    temp = [brackets[i][0] for i in range(n)]
    string = "".join(temp)
    answer = calcAnswer(string)

    print(answer)

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

        brackets[i] = [brackets[i], left, right]

if __name__=="__main__":
    n = int(input())
    brackets = [
        input().strip()
        for _ in range(n)
    ]

    preprocessing(brackets)

    greedy(brackets)