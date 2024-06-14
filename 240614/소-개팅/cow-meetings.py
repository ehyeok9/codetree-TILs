from collections import deque

def simulation(information, characteristic):
    deq = deque(information)
    count = 0

    while len(deq) > 1:
        count += 1        
        key, cnt = max(characteristic.items(), key=lambda x: x[1])
        idx, end = 0, len(deq)

        while deq:
            if idx == end: break
            idx += 1
            e,k = deq.popleft()
            
            if key in k:
                deq.append([e,k])
            else:
                minusVals(characteristic, k)
        
        characteristic.pop(key, None)
    
    print(count)

def minusVals(characteristic, keys):
    for key in keys:
        if key in characteristic:
            characteristic[key] -= 1
            if characteristic[key] == 0:
                characteristic.pop(key, None)


n = int(input())

information = []
characteristic = dict()
for _ in range(n):
    e, k, *character = input().split()
    information.append([e, character])
    
    for char in character:
        characteristic[char] = characteristic.setdefault(char,0) + 1

simulation(information, characteristic)