import sys

input = sys.stdin.readline

INT_MAX = sys.maxsize

def calc(houses, idx):
    global n
    
    distance = 0
    for i in range(n):
        distance += abs(i + 1 - idx) * houses[i]
    
    return distance
    

if __name__=="__main__":
    n = int(input())
    houses = list(map(int, input().split()))
    
    result = INT_MAX
    for i in range(n):
        temp = calc(houses, i+1)
        result = min(result, temp)
    
    print(result)