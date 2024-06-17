def dfs(cows, character, characterList, visited, count, cur):
    global answer
    # print(cows)
    # print(visited, characterList)
    # print(count)
    
    if (count > answer): answer = count
    if (len(cows) <= 1): return

    for i in range(cur, len(characterList)):
        if visited[i] == False:
            yesList = set(character[characterList[i]])
            visited[i] = True
            dfs(yesList & cows, character, characterList, visited, count + 1, i+1)
            visited[i] = False



n = int(input())
character = dict()
cows = set()
for _ in range(n):
    e, k, *char = input().split()
    cows.add(e)
    for c in char:
        character[c] = character.setdefault(c, []) + [e]
        
characterList = list(character.keys())
answer = -1
visited = [False for _ in range(len(characterList))]

dfs(cows, character, characterList, visited, 0, 0)

print(answer)