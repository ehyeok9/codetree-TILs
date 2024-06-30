import sys

input = sys.stdin.readline

result = 0

def dfs(N, cows, chars, visited, cnt):
    global result
    
    if (cnt > result):
        result = cnt

    if (getCount(cows, visited) <= 1): return

    for char in chars:
        if char in visited: continue
        visited.add(char)
        dfs(N, cows, chars, visited, cnt+1)
        visited.remove(char)

def getCount(cows, visited):
    cnt = 0
    for name, num, chars in cows:
        if len(chars & visited) == len(visited):
            cnt += 1
    return cnt

if __name__=="__main__":
    N = int(input())
    cows = []
    chars = set()
    for _ in range(N):
        name, cnt, *char = input().split()
        cows.append([name, int(cnt), set(char)])
        chars.update(char)
    
    dfs(N, cows, chars, set(), 0)
    
    print(result)