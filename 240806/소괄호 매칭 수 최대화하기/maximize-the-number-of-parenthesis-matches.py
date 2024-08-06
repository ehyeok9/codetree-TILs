import sys

input = sys.stdin.readline

def greedy(brackets):
    global n

    brackets.sort(key = lambda x : (-x[3], x[2], -x[1]))
    temp = [brackets[i][0] for i in range(n)]
    string = "".join(temp)
    # print(brackets)
    # print(string)
    answer = calcAnswer(string)

    print(answer)

# (3, 2, 1) / (1,0,1) / (1,1,0) / (4,0,4)

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

        brackets[i] = [brackets[i], left, right, left - right]

if __name__=="__main__":
    n = int(input())
    brackets = [
        input().strip()
        for _ in range(n)
    ]

    preprocessing(brackets)

    greedy(brackets)