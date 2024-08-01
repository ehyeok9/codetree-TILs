import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    jewels = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    
    for i in range(n):
        w, v = jewels[i]
        jewels[i].append(v/w)
    
    jewels.sort(key = lambda x : x[2], reverse=True)
    
    answer = 0
    curWeight = 0
    for w, v, vpw in jewels:
        if curWeight + w <= m:
            curWeight += w
            answer += v
        else:
            answer += vpw * (m - curWeight)
            curWeight = m
            break
    
    print("%.3f" % answer)
    # print(jewels)