from collections import deque

n, x = map(int, input().split())
nums = list(map(int, input().split()))
deq = deque(zip(range(0, n), nums))

vals = list(set(nums))
valCounts = [nums.count(val) for val in vals]
dictionary = dict(zip(vals, valCounts))
keys = sorted(dictionary.keys(), reverse=True)
cur = 0

count = 0
while deq:
    idx, num = deq.popleft()
    val = keys[cur]

    if num == val:
        dictionary[val] -= 1
        count += 1
        if idx == x:
            print(count)
            break
    else:
        deq.append([idx, num])
    
    if dictionary[val] == 0:
        cur += 1