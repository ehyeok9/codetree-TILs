import sys

input = sys.stdin.readline

def greedy(bomb):
    global n
    answer = 0

    bomb.sort(key = lambda x : (-x[0], x[1]))
    time = [0 for _ in range(10001)]
    # print(bomb)

    for i in range(n):
        point, limit = bomb[i]
        count = sum(time[:limit+1])
        if check(count, time, limit, i+1):
            answer += point
            time[limit] += 1
            # print(answer, limit, i+1)

    return answer

def check(count, time, limit, end):
    if count >= limit: return False
    
    temp = count
    for num in range(limit+1, end+1):
        temp += time[num]
        # print(num, temp)
        if temp >= num: return False
    
    return True

if __name__=="__main__":
    n = int(input())
    bomb = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    print(greedy(bomb))