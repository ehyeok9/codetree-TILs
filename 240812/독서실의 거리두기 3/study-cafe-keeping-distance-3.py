import sys

input = sys.stdin.readline

def getDistance(seats):
    global n

    distance = []
    start = 0
    for i in range(1,n):
        if seats[i] == '0': continue
        distance.append([start, i, i-start])
        start = i
    
    return distance

if __name__=="__main__":
    n = int(input())
    seats = list(input().strip())
    
    distance = getDistance(seats)
    distance.sort(key = lambda x : -x[2])

    for start, end, dist in distance:
        if dist == 1: continue
        mid = (start + end) // 2
        seats[mid] = '1'
        break
    
    distance = getDistance(seats)
    distance.sort(key = lambda x : x[2])
    # print(seats)
    print(distance[0][2])