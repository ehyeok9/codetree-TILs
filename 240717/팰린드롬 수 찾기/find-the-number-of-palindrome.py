import sys

input = sys.stdin.readline

def solution():
    global x, y
    
    answer = getPreCalc(x)
    
    plus = [0,0,0,1,1,2,2,3]
    for i in range(len(x)+1, len(y)):
        answer += 9 * pow(10, plus[i])

    if len(y) != 7:
        answer += getAfterCalc(y)

    print(answer)

    # 10의자리 11 22 33 -> 9개 : 1 
    # 100의자리 101 111 212 313 -> 10 * 9 : 1
    # 1000의자리 1001 2112 -> 10 * 9 : 2 
    # 10000의자리 10001 -> 10 * 10 * 9 : 2

def getAfterCalc(y):
    length = (len(y)//2 + 1) if (len(y)%2 == 1) else (len(y)//2)
    result = 1

    for i in range(length):
        temp = min(int(y[i]), int(y[len(y) - 1 - i]))
        if i != 0: temp += 1
        result *= temp
        # print(temp)
    
    return result

def getPreCalc(x):
    preCalc = []
    length = (len(x)//2 + 1) if (len(x)%2 == 1) else (len(x)//2)

    for i in range(length):
        preCalc.append(max(int(x[i]), int(x[len(x) - 1 - i])))

    answer = 1
    for i in range(len(preCalc)):
        answer *= (10 - preCalc[i])

    return answer

if __name__ == "__main__":
    x, y = input().split()
    
    solution()