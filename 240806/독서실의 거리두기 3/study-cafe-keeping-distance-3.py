import sys

input = sys.stdin.readline

def getMinimum(seats):
    answer = float("inf")
    for i in range(len(seats)):
        if seats[i] == "": continue
        answer = min(len(seats[i]), answer)
    
    if answer == float("inf"):
        return 0
    return answer

if __name__=="__main__":
    n = int(input())
    seats = input().split('1')
    minimumLength = getMinimum(seats)
    
    temp = list('0' * minimumLength)
    temp[len(temp)//2] = '1'
    nextString = "".join(temp).split('1')

    print(min(minimumLength, getMinimum(nextString)) + 1)