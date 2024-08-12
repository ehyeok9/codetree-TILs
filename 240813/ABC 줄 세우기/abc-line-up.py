import sys

input = sys.stdin.readline

global n

def getDistance(alphabets):
    distance = []
    for i in range(n):
        targetLoc = ord(alphabets[i]) - ord('A')
        dist = abs(targetLoc - i)
        
        if dist != 0: 
            distance.append([i, targetLoc, abs(targetLoc - i)])

    return distance

if __name__ == "__main__":
    n = int(input())
    alphabets = input().split()
    
    result = 0
    while True:
        distance = getDistance(alphabets)
        if (distance == []): break
        distance.sort(key = lambda x : x[2])
        a, b, d = distance[0]
        alphabets[a], alphabets[b] = alphabets[b], alphabets[a]
        result += 1
    
    print(result)
    
    # 인접한 2개 -> 위치랑 거리가 가까운 것부터 바꾼다
    # 0 0 0
    # 1 3 2
    # 2 1 1
    # 3 2 1