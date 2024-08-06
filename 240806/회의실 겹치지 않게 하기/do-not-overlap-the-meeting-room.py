import sys

input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    meetings = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    meetings.sort(key = lambda x : (-x[1], -x[0]))
    # print(meetings)
    answer = 1
    prev = meetings[0][0]
    for i in range(1, n):
        start, end = meetings[i]
        if end <= prev:
            answer += 1
            prev = start

    print(n - answer)