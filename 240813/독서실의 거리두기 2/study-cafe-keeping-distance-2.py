import sys

input = sys.stdin.readline

global n

def getDistances(seats):
    distances = []
    start = 0
    
    for i in range(1, n):
        if seats[i] == '0':
            left = calcDistance(seats, i, -1)
            right = calcDistance(seats, i, 1)
            distances.append([i, min(left, right)])
    
    return distances

def calcDistance(seats, cur, direct): 
    cnt = 1
    cur += direct
    while (0 <= cur < n):
        if (seats[cur] == '1'): return cnt
        cur += direct
        cnt += 1
    
    return float("inf")

def getMinumumDist(seats):
    prev = 0
    result = float("inf")
    for i in range(1, n):
        if seats[i] == '1':
            result = min(result, i - prev)
            prev = i

    return result

if __name__ == "__main__":
    n = int(input())
    seats = list(input().strip())

    distances = getDistances(seats)
    distances.sort(key = lambda x : -x[1])
    
    seats[distances[0][0]] = '1'
    # print(distances)
    # print("".join(seats))
    print(getMinumumDist(seats))