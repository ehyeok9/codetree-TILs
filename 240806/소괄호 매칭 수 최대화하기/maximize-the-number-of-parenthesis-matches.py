import sys

input = sys.stdin.readline

def greedy(brackets):
    global n

    brackets.sort(key = lambda x : -x[1])
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
        point = brackets[i].count('(') - brackets[i].count(')')
        brackets[i] = [brackets[i], point]

if __name__=="__main__":
    n = int(input())
    brackets = [
        input().strip()
        for _ in range(n)
    ]

    preprocessing(brackets)

    greedy(brackets)